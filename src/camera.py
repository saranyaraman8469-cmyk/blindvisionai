import cv2

def start_camera():
    # Try default webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("[CAMERA] Failed to open camera")
        return None

    print("[CAMERA] Camera opened successfully")
    return cap


def show_camera(cap):
    if cap is None:
        return

    ret, frame = cap.read()

    if not ret or frame is None:
        print("[CAMERA] Failed to read frame")
        return

    cv2.imshow("BlindVisionAI - Camera View", frame)
    cv2.waitKey(1)


def stop_camera(cap):
    if cap:
        cap.release()
    cv2.destroyAllWindows()
    print("[CAMERA] Camera stopped")
