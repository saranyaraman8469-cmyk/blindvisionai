import cv2
import numpy as np
import time

class ObstacleDetector:
    def __init__(self):
        self.prev_gray = None
        self.last_motion_time = time.time()

    def detect(self, frame):
        h, w, _ = frame.shape

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return "NO MOTION"

        diff = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

        self.prev_gray = gray

        # Split regions
        left = thresh[:, :w//3]
        front = thresh[:, w//3:2*w//3]
        right = thresh[:, 2*w//3:]
        back = thresh[h//2:, :]

        # Motion scores
        left_score = np.sum(left)
        front_score = np.sum(front)
        right_score = np.sum(right)
        back_score = np.sum(back)

        total_motion = left_score + front_score + right_score + back_score

        # ---- DECISION LOGIC ----

        if total_motion < 500_000:
            return "NO MOTION"

        # Strong obstacle in front → STOP
        if front_score > 1_500_000:
            return "STOP"

        # Obstacle directions
        if left_score > right_score and left_score > 700_000:
            return "MOVE RIGHT"

        if right_score > left_score and right_score > 700_000:
            return "MOVE LEFT"

        if back_score > 700_000:
            return "MOVE FORWARD"

        # Mild motion only
        if total_motion < 1_200_000:
            return "PATH CLEAR"

        return "NO MOTION"
