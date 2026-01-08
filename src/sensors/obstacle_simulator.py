import random

def detect_obstacle():
    """
    Simulates obstacle detection
    """
    options = [
        "FRONT",
        "LEFT",
        "RIGHT",
        "BACK",
        "CLEAR",
        "NO_MOTION"
    ]
    return random.choice(options)
