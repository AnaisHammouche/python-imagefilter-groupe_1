import cv2
import logger


def filter_gray_scale(img):
    '''
    Apply a filter into a picture
    :param img: String, file to filter
    :return: the filtered picture
    '''
    logger.log('Apply the filter grayscale')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
