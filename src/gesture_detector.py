import cv2
import numpy as np

class GestureDetector:
    def __init__(self):
        self.prev_gray = None

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (15, 15), 0)

        if self.prev_gray is None:
            self.prev_gray = gray
            return "NO MOTION"

        diff = cv2.absdiff(self.prev_gray, gray)
        thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]

        self.prev_gray = gray

        ys, xs = np.where(thresh > 0)

        if len(xs) < 3000:
            return "NO MOTION"

        avg_x = np.mean(xs)
        avg_y = np.mean(ys)

        h, w = gray.shape

        if avg_x < w * 0.4:
            return "MOVE LEFT"
        elif avg_x > w * 0.6:
            return "MOVE RIGHT"
        elif avg_y < h * 0.4:
            return "MOVE FORWARD"
        elif avg_y > h * 0.6:
            return "MOVE BACKWARD"

        return "PATH CLEAR"
