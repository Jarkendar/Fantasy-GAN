from __future__ import absolute_import, division, print_function, unicode_literals

import os
import cv2
import re
import random

IMAGES_DIR = './dataset'
LEARN = False


#LISTING PLIKÓW -> DATASET fromatensorslice -> w tensor flow
#TTENSOR GFLOW
class MockNetwork:
    name = 'Fake Network'

    def __init__(self, classes):
        self.classes = classes

    def generate(self, img):
        return img

    def predict(self, img):
        return random.choice(self.classes)


def network(labeled_images):
    return


def read_image(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def get_labels(name):
    return [c for c in name.split('_') if not re.match('[0-9.]', c)]


def read_images_with_labels(path):
    return [(read_image(path + '/' + name), get_labels(name)) for name in os.listdir(path)]


def save_image(image, path):
    cv2.imwrite(path, image)


def main():
    images_with_labels = read_images_with_labels(IMAGES_DIR)  # ~ 8gb ram required

    classes = set()
    for (_, c) in images_with_labels:
        [classes.add(i) for i in c]
    # todo network in this place

    if(LEARN):
        # todo learn
        pass
    else:
        mock_network = MockNetwork([item for item in classes])
        print(mock_network.classes)

        print(mock_network.predict(images_with_labels[0][0]))
        save_image(mock_network.generate(images_with_labels[0][0]), 'test.jpg')

    print(images_with_labels[0])
    print(len(images_with_labels))


if __name__ == '__main__':
    main()
