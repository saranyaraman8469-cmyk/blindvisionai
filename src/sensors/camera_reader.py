import cv2

class Camera:
    def __init__(self):
        print("[CAMERA] Initializing...")
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            raise RuntimeError("Camera not accessible")

        print("[CAMERA] Camera opened ✅ (LED ON)")

    def start_preview(self):
        print("[CAMERA] Preview started")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            cv2.imshow("BlindVisionAI - Camera", frame)

            # Press Q to close preview manually
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print("[CAMERA] Camera released ❌")
