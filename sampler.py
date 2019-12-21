import os
import cv2

DEFAULT_EXT = 'jpg'


def read_image(path):
    return cv2.imread(path)


def save_img(img, name):
    cv2.imwrite('./sampled_dataset/' + name, img)


def main():
    for i, filePath in enumerate(os.listdir('./dataset')):
        if i % 10 == 0:
            img = read_image('./dataset/' + filePath)
            save_img(img, filePath)


if __name__ == '__main__':
    main()
