import time
import random

def read_imu():
    """
    Simulate IMU sensor data
    """
    return {
        "acceleration": random.uniform(0.0, 1.5),
        "gyroscope": random.uniform(-180, 180),
        "timestamp": time.time()
    }

def fuse_camera_imu(camera_data, imu_data):
    """
    Sensor fusion logic
    """
    return {
        "obstacle_position": camera_data,
        "user_motion": imu_data
    }

if __name__ == "__main__":
    camera_output = {"x": 2, "y": 3}
    imu_output = read_imu()

    fused = fuse_camera_imu(camera_output, imu_output)
    print("Fused Sensor Output:", fused)
