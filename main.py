from filters import filter_gray_scale
from filters import filter_dilate
from filters import filter_blur
import os
import cv2
import numpy as np


# VERIF FORMAT IMAGE
def get_all_images_link():
    for files in os.walk("assets/"):
        for filename in files:
            filename
    return filename


def valid_format():
    all_links = get_all_images_link()
    for x in all_links:
        extension = os.path.splitext('assets/' + x)
        if not (extension[1] in (".jpg", ".png")):
            return f'The pictures {x} has wrong format'
    return True


# VERIF FICHIER DANS LE DOSSIER
def file_exist():
    files = get_all_images_link()
    length = len(files)
    if length == 0:
        return f'The directory has {length} image(s)'
    return True


# Create output if not already exist
def create_output():
    if not os.path.exists('output'):
        os.mkdir('output')


def apply_filter(filters, nb=None):
    apply = filters.split('|')
    numb = None
    for y in apply:
        if ":" in y:
            numb = y.split(":")
    all_img = get_all_images_link()
    create_output()
    if file_exist() and valid_format():
        for x in all_img:
            image = cv2.imread('assets/' + x)
            if 'dilate' in filters:
                image = filter_dilate.filter_dilate(image, int(numb[1]))
            if 'blur' in filters:
                image = filter_blur.filter_blur(image, int(numb[1]))
            if 'grayscale' in filters:
                image = filter_gray_scale.filter_gray_scale(image)
            cv2.imwrite(f'output/{x}', image)
    else:
        return valid_format() or create_output()


print("++++++++++++++++++++++++++++++++++")

# apply_filter(('grayscale', 'dilate', 'blur'), 21)

# image = cv2.imread('assets/' + img)

# cv2.imwrite(f'output/{img}', blur)

# cv2.imwrite(f'output/{img}', erosion)

# cv2.imwrite(f'output/{img}', gray)
