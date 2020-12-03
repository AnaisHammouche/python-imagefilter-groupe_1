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
            return f'L\'image {x} n\'a pas le bon format'
    return True


# VERIF FICHIER DANS LE DOSSIER
def file_exist():
    files = get_all_images_link()
    length = len(files)
    if length == 0:
        return f'Le dossier contient {length} image(s)'
    return True


# Create output if not already exist
def create_output():
    if not os.path.exists('output'):
        os.mkdir('output')


# CALL ALL IMAGE
def do_all_images_gray_scale():
    all_img = get_all_images_link()
    create_output()
    print('DEBUT')
    for x in all_img:
        filter_gray_scale.filter_gray_scale(x)
    print('FINI')


def do_all_images_blur(nb):
    all_img = get_all_images_link()
    create_output()
    print('DEBUT')
    for x in all_img:
        filter_blur.filter_blur(x, nb)
    print('FINI')


def do_all_images_dilate(nb):
    all_img = get_all_images_link()
    create_output()
    for x in all_img:
        filter_dilate.filter_dilate(x, nb)


def call_filter(filter_name, nb=-1):
    if True in (create_output(),valid_format()):
        if filter_name == 'blur':
            do_all_images_blur(nb)
        elif filter_name == 'dilate':
            do_all_images_dilate(nb)
        elif filter_name == 'grayscale':
            do_all_images_gray_scale()
            print("ok")
        else:
            print('Filter do not exist !\nblur:<number>\ndilate:<number>\ngrayscale')
    else:
        return valid_format() or create_output()


print("++++++++++++++++++++++++++++++++++")


#do_all_images_blur(21)

