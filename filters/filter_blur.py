import cv2


def filter_blur(img, nb):
    if (nb > 2) & (nb % 2 != 0):
        image = cv2.imread('assets/' + img)
        blur = cv2.GaussianBlur(image, (nb, nb), cv2.BORDER_DEFAULT)
        cv2.imwrite(f'output/{img}', blur)
    elif nb <= 1:
        print("Valeur du flou trop faible")
        return None
    else:
        print("Entrer une valeur impaire")
        return None
