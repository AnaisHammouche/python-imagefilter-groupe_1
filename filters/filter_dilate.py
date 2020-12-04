import cv2
import numpy as np
import logger


def filter_dilate(img, nb):
    '''
    Apply filter on picture
    :param img: String, file to filter
    :param nb: Int, value of dilate to apply
    :return: the filtered picture
    '''
    logger.log('Apply the filter dilate')
    if nb >= 0:
        kernel = np.ones((nb, nb), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
        return erosion
    else:
        print("Value is negative, please enter positive number")
        return None
