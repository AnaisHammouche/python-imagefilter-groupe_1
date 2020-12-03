import cv2
import numpy as np


def filter_dilate(img, nb):
    if nb >= 0:
        image = cv2.imread('assets/' + img)
        kernel = np.ones((nb, nb), np.uint8)
        erosion = cv2.erode(image, kernel, iterations=1)
        cv2.imwrite(f'output/{img}', erosion)
    else:
        print("Valeur négative non accepter")
        return None
