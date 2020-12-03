import cv2


def filter_gray_scale():
    image = cv2.imread('../assets/homer.jpeg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('../assets.test.jpg', gray)
    cv2.imshow('Original image', image)
    cv2.imshow('Gray image', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

filter_gray_scale()