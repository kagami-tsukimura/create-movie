import argparse
import os
import random
from enum import Enum
from glob import glob

import cv2

# import numpy as np


class Image(Enum):
    BACKGROUND = "background"
    OVERLAY = "overlay"


def setting_args():
    """Parse command line arguments for the merge images.

    Returns:
        Namespace: Containing parsed arguments.
    """

    parser = argparse.ArgumentParser(description="merge images")
    parser.add_argument("-n", "--N", default=10, type=int)
    return parser.parse_args()


# OpenCVで、指定した座標に2つの画像を合成する処理。
# def merge_images(img1, img2, x, y):
#     """Merge two images into one.

#     Args:
#         img1 (numpy.ndarray): The first image.
#         img2 (numpy.ndarray): The second image.
#         x (int): The x coordinate to place the second image.
#         y (int): The y coordinate to place the second image.

#     Returns:
#         numpy.ndarray: The merged image.
#     """
#     # The second image is placed at the specified coordinates.
#     img1[y : y + img2.shape[0], x : x + img2.shape[1]] = img2
#     return img1


def main(args):
    """Main function for the merge images.

    Args:
        args (argparse.Namespace): Containing parsed arguments.
    """

    IMG_DIR = "../crawler/ml/images/"
    BG_DIR = os.path.join(os.path.dirname(IMG_DIR, Image.BACKGROUND.value))
    OVER_DIR = os.path.join(os.path.dirname(IMG_DIR, Image.OVERLAY.value))

    choice_bg = random.choice(glob(f"{BG_DIR}/*"))
    choice_over = random.choice(glob(f"{OVER_DIR}/*"))


def save_image(img, file_name):
    """Save the image.

    Args:
        img (numpy.ndarray): The image to save.
        file_name (str): The file name to save.
    """

    cv2.imwrite(file_name, img)


# OpenCVでランダムにx座標とy座標を生成する処理。
def random_position(img1, img2):
    """Generate random coordinates.

    Args:
        img1 (numpy.ndarray): The first image.
        img2 (numpy.ndarray): The second image.

    Returns:
        int: The x coordinate.
        int: The y coordinate.
    """

    # The second image is placed at the specified coordinates.
    x = random.randint(0, img1.shape[1] - img2.shape[1])
    y = random.randint(0, img1.shape[0] - img2.shape[0])
    return x, y


if __name__ == "__main__":
    args = setting_args()
    main(args)
