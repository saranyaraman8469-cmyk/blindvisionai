import cv2
from sensors.camera_reader import Camera

cam = Camera()

def detect_obstacle():
    frame = cam.get_frame()

    if frame is None:
        return False

    cv2.imshow("BlindVision Camera", frame)

    # Dummy logic (replace with ML later)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()

    if brightness < 80:
        return True
    return False
