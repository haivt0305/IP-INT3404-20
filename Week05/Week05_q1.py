"""
Name: Vo Thanh Hai
Class: INT3404 20
MSSV: 18020452
You should understand the code you write.
"""


import cv2
import numpy as np
import time
import statistics

def conv_sum(a, b):
    s = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            s += a[i][j]*b[i][j]
    return s


def convolution_mean_filter(I, g, mode='valid', boundary='zero_padding'):
    h, w = len(g), len(g[0])
    H, W = I.shape[0], I.shape[1]

    if mode == 'valid':
        output_h = H - (h - 1)
        output_w = W - (w - 1)
    else:
        output_h = H
        output_w = W

    output = [[0 for _ in range(output_w)] for _ in range(output_h)]
    for i in range(output_h):
        for j in range(output_w):
            output[i][j] = conv_sum(I[i:i + h, j:j + w], g)

    return output


def init_kernel(sz):
    s = sz*sz
    g = [[1.0/s for i in range(sz)] for i in range(sz)]

    return g


def mean_filter(input_file, output_file, kernel_size):
    # Read input file with gray value
    img = cv2.imread(input_file, 0)
    g = init_kernel(kernel_size)

    start_time = time.time()
    output_img = convolution_mean_filter(img, g)
    run_time = time.time() - start_time

    # for input/output
    cv2.imwrite(output_file, np.array(output_img))
    print("Run convolution in: %.2f s" % run_time)


def median_value(a, b):
    x = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            x.append(a[i][j])
    x.sort()
    med = statistics.median(x)
    return med


def convolution_median_filter(I, g, mode='valid', boundary='zero_padding'):
    h, w = len(g), len(g[0])
    H, W = I.shape[0], I.shape[1]

    if mode == 'valid':
        output_h = H - (h - 1)
        output_w = W - (w - 1)
    else:
        output_h = H
        output_w = W

    output = [[0 for _ in range(output_w)] for _ in range(output_h)]
    for i in range(output_h):
        for j in range(output_w):
            output[i][j] = median_value(I[i:i + h, j:j + w], g)

    return output


def median_filter(input_file, output_file, kernel_size):
    img = cv2.imread(input_file, 0)
    g = init_kernel(kernel_size)

    output_img = convolution_median_filter(img, g)
    cv2.imwrite(output_file, np.array(output_img))


def init_kernel_sharpen_filter(sz):
    s = sz*sz
    g = [[1.0/s for i in range(sz)] for i in range(sz)]
    g[sz%2][sz%2] = 1.0

    return g


def sharpen_filter(input_file, output_file, kernel_size):
    img = cv2.imread(input_file)
    g = init_kernel(kernel_size)
    gs = init_kernel_sharpen_filter(kernel_size)

    output_img = convolution_mean_filter(np.array(convolution_mean_filter(img, gs)), (np.array(gs) + 5 * (np.array(gs)-np.array(g))))
    cv2.imwrite(output_file, np.array(output_img))


if __name__ == '__main__':

    #mean_filter('font.png', 'mean-filter-font.png', 3)
    #median_filter('font.png', 'median-filter-font.png', 3)
    sharpen_filter('font.png', 'sharpen-filter-font.png', 3)
