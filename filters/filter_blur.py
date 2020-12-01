import cv2


def filter_blur(nb):
    image = cv2.imread('../assets/homer.jpeg')
    blur = cv2.GaussianBlur(image, (nb, nb), cv2.BORDER_DEFAULT)
    cv2.imshow('Original image', image)
    cv2.imshow('Blur image', blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


filter_blur(145)

# faire attention au nombre pair