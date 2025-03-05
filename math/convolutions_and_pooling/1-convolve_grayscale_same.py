#!/usr/bin/env python3


"""Importing necessary modules"""
import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.
    images: numpy.ndarray containing multiple grayscale images
    m: number of images
    h: height in pixels of the images
    w: width in pixels of the images
    kernel: numpy.ndarray containing the kernel for the convolution
    kh: height of the kernel
    kw: width of the kernel
    Returns: numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # # Calculate the padding required to maintain the same output size
    # padding_h = kh // 2
    # padding_w = kw // 2
    # padded_images = np.pad(
    #     images, ((0, 0), (padding_h, padding_h), (padding_w, padding_w)),
    #     mode='constant')

    # # Perform convolution
    # convolved_images = np.zeros((m, h, w))
    # for i in range(m):
    #     for j in range(h):
    #         for k in range(w):
    #             patch = padded_images[i, j:j + kh, k:k + kw]
    #             convolved_images[i, j, k] = np.sum(patch * kernel)
    #             print(convolved_images)

    # return convolved_images

    m, hm, wm = images.shape
    ph = int(kh / 2)
    pw = int(kw / 2)
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    convoluted = np.zeros((m, hm, wm))
    for h in range(hm):
        for w in range(wm):
            square = padded[:, h: h + kh, w: w + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
