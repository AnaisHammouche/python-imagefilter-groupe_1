import cv2


def filter_gray_scale(img):
    image = cv2.imread('assets/' + img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f'output/{img}', gray)
