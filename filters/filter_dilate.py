import cv2
import numpy as np


def filter_dilate(nb):
    image = cv2.imread('../assets/homer.jpeg')
    kernel = np.ones((nb, nb), np.uint8)
    erosion = cv2.erode(image, kernel, iterations=1)
    cv2.imshow('Image de base', image)
    cv2.imshow('Blur image', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filter_dilate(1)

