import cv2
import numpy as np


def filter_dilate(img, nb):
    if nb >= 0:
        kernel = np.ones((nb, nb), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
        return erosion
    else:
        print("Value is negative, please enter positive number")
        return None
