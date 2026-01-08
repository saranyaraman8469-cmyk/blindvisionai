import cv2
import numpy as np
from sensors.camera_reader import Camera

cam = Camera()
prev_frame = None

def detect_obstacle():
    global prev_frame

    frame = cam.get_frame()
    if frame is None:
        return False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if prev_frame is None:
        prev_frame = gray
        return False

    # Difference between frames
    frame_delta = cv2.absdiff(prev_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    motion_pixels = np.sum(thresh) / 255

    prev_frame = gray

    cv2.imshow("BlindVision Motion", thresh)

    # Threshold for obstacle
    if motion_pixels > 5000:
        return True
    return False
