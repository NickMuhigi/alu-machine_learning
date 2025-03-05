#!/usr/bin/env python3
"""Importing necessary modules"""
import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a convolution on grayscale images.

    Args:
    images: with shape (m, h, w) containing multiple grayscale images.
    kernel: with shape (kh, kw) containing the kernel for the convolution.
    padding:either a tuple of (ph, pw), 'same', or 'valid'.
    stride: sh is the stride for the height and sw is the stride for the width.

    Returns:
    numpy.ndarray: containing the convolved images.
    """
    kh, kw = kernel.shape
    m, hm, wm = images.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(((hm - 1) * sh + kh - hm) / 2) + 1
        pw = int(((wm - 1) * sw + kw - wm) / 2) + 1
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw)), 'constant')
    ch = int((hm + 2 * ph - kh) / sh) + 1
    cw = int((wm + 2 * pw - kw) / sw) + 1
    convoluted = np.zeros((m, ch, cw))
    for h in range(ch):
        for w in range(cw):
            square = padded[:, h * sh: h * sh + kh, w * sw: w * sw + kw]
            insert = np.sum(square * kernel, axis=1).sum(axis=1)
            convoluted[:, h, w] = insert
    return convoluted
