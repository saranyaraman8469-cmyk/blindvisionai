import cv2

def detect_obstacle():
    cap = cv2.VideoCapture(0)

    ret, frame = cap.read()
    cap.release()

    if not ret:
        return None, None

    height, width, _ = frame.shape

    # Simple heuristic (center region)
    center_region = frame[:, width//3:2*width//3]
    gray = cv2.cvtColor(center_region, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

    mean_intensity = blur.mean()

    # Fake distance approximation
    distance = 1.5 if mean_intensity > 120 else 0.6
    direction = "front"

    return distance, direction
