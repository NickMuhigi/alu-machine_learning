#!/usr/bin/env python3
""" Importing necessary modules"""
import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding
    images: numpy.ndarray containing myltiple grayscale images
    m: number of images
    h: height in pixels of the images
    w: width in pixels of the images
    kernel: numpy.ndarray containing the kernel for the convolution
    kh: height of the kernel
    kw: width of the kernel
    padding: tuple containing padding of images
    ph: height of padding
    pw: width of padding
    Returns: numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')

    convolved_h = (h + 2 * ph - kh + 1)
    convolved_w = (w + 2 * pw - kw + 1)

    convolved_images = np.zeros((m, convolved_h, convolved_w))
    for i in range(convolved_h):
        for j in range(convolved_w):
            convolved_images[:, i, j] = np.sum(padded[:, i:i+kh, j:j+kw] *
                                               kernel, axis=(1, 2))
    return convolved_images
