import cv2


def filter_blur(img, nb):
    if (nb > 2) & (nb % 2 != 0):
        blur = cv2.GaussianBlur(img, (nb, nb), cv2.BORDER_DEFAULT)
        return blur
    elif nb <= 1:
        print("Value too small")
        return None
    else:
        print("Please enter negative value")
        return None
