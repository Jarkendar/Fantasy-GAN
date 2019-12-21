import os
import cv2
from numpy import shape

OUTPUT_DIR = './Resized_image'
DEFAULT_EXT = 'jpg'
RESIZED_SIZE = 256


def save_img(img, path, name='test', number=0, ext='jpg'):
    cv2.imwrite(path + '/' + name + '_' + str(number) + '.' + ext, img)


def resize_img(img, square_side):
    return cv2.resize(img, (square_side, square_side))


def cut_side_column_img(img):
    width, height = shape(img)[0], shape(img)[1]
    difference = int((height - width) / 2)
    return img[:, difference: width + difference]


def read_image(path='./Images/elf_archer/elf_archer_0.jpg'):
    return cv2.imread(path)


def make_all(path):
    for directory in os.listdir(path):
        print(directory)
        for i, imageName in enumerate(os.listdir(path + '/' + directory)):
            img = read_image(path + '/' + directory + '/' + imageName)
            cut_img = cut_side_column_img(img)
            smaller_img = resize_img(cut_img, RESIZED_SIZE)
            save_img(smaller_img, OUTPUT_DIR, directory, i, DEFAULT_EXT)


def create_output_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def main():
    create_output_dir(OUTPUT_DIR)
    make_all('./Images')


if __name__ == '__main__':
    main()
