import cv2
import numpy as np

def bird_eye_view(image):
    """
    Convert camera image to Bird's Eye View (BEV)
    """

    height, width = image.shape[:2]

    # Define source points (camera view)
    src = np.float32([
        [0, height],
        [width, height],
        [width * 0.8, height * 0.6],
        [width * 0.2, height * 0.6]
    ])

    # Define destination points (top-down view)
    dst = np.float32([
        [0, height],
        [width, height],
        [width, 0],
        [0, 0]
    ])

    matrix = cv2.getPerspectiveTransform(src, dst)
    bev = cv2.warpPerspective(image, matrix, (width, height))

    return bev


if __name__ == "__main__":
    img = cv2.imread("sample.jpg")  # add any test image
    bev = bird_eye_view(img)

    cv2.imshow("Original", img)
    cv2.imshow("Bird Eye View", bev)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
