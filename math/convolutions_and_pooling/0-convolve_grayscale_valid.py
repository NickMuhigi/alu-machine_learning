#!/usr/bin/env python3


"""Importing necessary modules"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    This function performs a valid convolution on grayscale images.
    Images: numpy.ndarray containing multiple grayscale images
    m: number of images
    h: height in pixels of the images
    w: width in pixels of the images
    kernel: numpy.ndarray containing the kernel for the convolution
    kh: height of the kernel
    kw: width of the kernel
    Returns: numpy.ndarray containing the convolved images
    """
    # Initialize variables for height and width
    m, h, w = images.shape
    kh, kw = kernel.shape

    new_h = h - kh + 1
    new_w = w - kw + 1

    convolved_images = np.zeros((m, new_h, new_w))

    for i in range(new_h):
        for j in range(new_w):
            convolved_images[:, i, j] = np.sum(images[:, i:i+kh, j:j+kw] *
                                               kernel, axis=(1, 2))

    return np.array(convolved_images)
