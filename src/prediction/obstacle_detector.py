import random
from sensors.camera_reader import Camera

camera = Camera()

def detect_obstacle():
    frame = camera.get_frame()
    if frame is None:
        return None

    return random.choice(
        ["FRONT", "LEFT", "RIGHT", "BACK", "CLEAR"]
    )
