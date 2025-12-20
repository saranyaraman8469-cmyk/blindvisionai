import time

def vibrate(intensity):
    """
    Simulate vibration intensity
    """
    print("Vibrating with intensity:", intensity)
    time.sleep(0.5)

if __name__ == "__main__":
    vibrate("HIGH")  # LOW / MEDIUM / HIGH
