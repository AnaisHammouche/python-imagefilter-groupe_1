import cv2

image = cv2.imread('lien image')

gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)