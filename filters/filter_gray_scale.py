import cv2


def filter_gray_scale(img):
    '''
    Apply a filter into a picture
    :param img: String, file to filter
    :return: the filtered picture
    '''
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray
