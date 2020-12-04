from filters import filter_gray_scale
from filters import filter_dilate
from filters import filter_blur
import os
import cv2
import logger
from configparser import ConfigParser


# VERIF FORMAT IMAGE
def get_all_images_link(link_img, link_log):
    '''
    Get all the file name in the directory assets
    :return: A Tuple with all file names
    '''
    logger.log('Get all links of directory', link_log)
    for files in os.walk(link_img):
        for filename in files:
            filename
    return filename


def valid_format(link_img, link_log):
    '''
    Check for all the files if the format is correct
    :return: True or an Error message
    '''
    logger.log('Check if the files formart is valid', link_log)
    all_links = get_all_images_link(link_img, link_log)
    for x in all_links:
        extension = os.path.splitext(link_img + x)
        if not (extension[1] in (".jpg", ".png")):
            return f'The pictures {x} has wrong format'
    return True


# VERIF FICHIER DANS LE DOSSIER
def file_exist(link_img, link_log):
    '''
    Check if the directory assets have an file in it
    :return: True or an Error message
    '''
    logger.log('Check if have any picture in the directory', link_log)
    files = get_all_images_link(link_img, link_log)
    length = len(files)
    if length == 0:
        return f'The directory has {length} image(s)'
    return True


# Create output if not already exist
def create_output(link_output, link_log):
    f'''
    Check if the directory {link_output} already exist if not create it
    '''
    logger.log(f'Check if the directory {link_output} exist', link_log)
    if not os.path.exists(link_output):
        os.mkdir(link_output)





def apply_filter(params):
    '''
    Apply all the require filter for the image
    :param params: Tuple with the args from CLI, and apply filter for each pictures
    '''
    link_img = "assets/"
    link_output = 'output/'
    link_log = 'image.log'
    params_filter = params
    logger.log('Function for aply filters', link_log)
    if '.' in params:
        parser = ConfigParser()
        parser.read(params)
        for section in parser.sections():
            print(section, " : ")
            # parcourt des paramètres et valeurs
            for name, value in parser.items(section):
                if name == 'input_dir':
                    print(f'{name} : {value}')
                    link_img = value
                if name == 'output_dir':
                    print(f'{name} : {value}')
                    link_output = value
                if name == 'log_file':
                    print(f'{name} : {value}')
                    link_log = value
                if name == 'content':
                    print(f'{name} : {value}')
                    params_filter = value

    apply = params_filter.split('|')
    numb = None
    for y in apply:
        if ":" in y:
            numb = y.split(":")
    all_img = get_all_images_link(link_img, link_log)
    create_output(link_output, link_log)
    if file_exist(link_img, link_log) and valid_format(link_img, link_log):
        for x in all_img:
            image = cv2.imread(link_img + x)
            if 'dilate' in params_filter:
                try:
                    image = filter_dilate.filter_dilate(image, int(numb[1]))
                except Exception as e:
                    print(numb[1])
            if 'blur' in params_filter:
                try:
                    image = filter_blur.filter_blur(image, int(numb[1]))
                except Exception as e:
                    print(numb[1])
            if 'grayscale' in params_filter:
                try:
                    image = filter_gray_scale.filter_gray_scale(image)
                except Exception as e:
                    print(numb[1])
            else:
                print("OK")
            cv2.imwrite(f'output/{x}', image)
    else:
        print(valid_format(link_img, link_log) or create_output(link_output, link_log))
