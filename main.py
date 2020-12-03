from filters import filter_gray_scale
from filters import filter_dilate
from filters import filter_blur
import os
import cv2


# VERIF FORMAT IMAGE
def get_all_images_link():
    '''
    Get all the file name in the directory assets
    :return: A Tuple with all file names
    '''
    for files in os.walk("assets/"):
        for filename in files:
            filename
    return filename


def valid_format():
    '''
    Check for all the files if the format is correct
    :return: True or an Error message
    '''
    all_links = get_all_images_link()
    for x in all_links:
        extension = os.path.splitext('assets/' + x)
        if not (extension[1] in (".jpg", ".png")):
            return f'The pictures {x} has wrong format'
    return True


# VERIF FICHIER DANS LE DOSSIER
def file_exist():
    '''
    Check if the directory assets have an file in it
    :return: True or an Error message
    '''
    files = get_all_images_link()
    length = len(files)
    if length == 0:
        return f'The directory has {length} image(s)'
    return True


# Create output if not already exist
def create_output():
    '''
    Check if the directory output already exist if not create it
    '''
    if not os.path.exists('output'):
        os.mkdir('output')


def apply_filter(filters):
    '''

    :param filters: Tuple with the args from CLI, and apply filter for each pictures
    '''
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
        print(valid_format() or create_output())
