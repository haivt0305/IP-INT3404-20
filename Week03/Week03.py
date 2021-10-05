
"""
Name: Vo Thanh Hai
Class: INT3404 20
MSSV: 18020452
You should understand the code you write.
"""

import numpy as np
import cv2
import argparse


def q_0(input_file, output_file, ):
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)
    cv2.imshow('Test img', img)
    cv2.waitKey(0)

    cv2.imwrite(output_file, img)

def q_1(input_file, output_file):
    """
    Convert the image to gray channel of the input image.
    """
    img = cv2.imread(input_file, cv2.IMREAD_COLOR)

    # Convert image to gray channgel

    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    img_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    cv2.imwrite(output_file, img_gray)

def q_2_opencv(input_file, output_file):
    """
    Performs a histogram equalization on the input image.
    """
    img = cv2.imread(input_file, 0)

    img_eq = cv2.equalizeHist(img)

    cv2.imshow('Test img', img_eq)
    cv2.waitKey(0)

    cv2.imwrite(output_file, img_eq)

def q_2_calculate(input_file, output_file):

    img = cv2.imread(input_file, 0)

    histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

    height, weight = img.shape
    histogram = histogram / (height * weight)

    histogram_cdf = np.cumsum(histogram)
    eq = (255 * histogram_cdf - 0.5).astype("uint8")

    img_eq = cv2.LUT(img, eq)

    cv2.imshow('Test img', img_eq)
    cv2.waitKey(0)

    cv2.imwrite(output_file, img_eq)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--input_file", "-i", type=str, help="1_test.jpg")
    # parser.add_argument("--output_file", "-o", type=str, help="Path to output image")
    # parser.add_argument("--question", "-q", type=int, default=0, help="Question number")
    #
    # args = parser.parse_args()
    #
    # q_number = args.question
    #
    # if q_number == 1:
    #     q_1(input_file=args.input_file, output_file=args.output_file)
    # elif q_number == 2:
    #     q_2(input_file=args.input_file, output_file=args.output_file)
    # else:
    #     q_0(input_file=args.input_file, output_file=args.output_file)

    q_2_opencv('peppers.png', 'peppers_eq.png')
    # q_2_calculate('peppers.png', 'peppers_eq.png')
