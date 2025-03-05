#!/usr/bin/env python3
"""
This module has the method that performs
convolution on grayscale images with channels
"""
import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performing convolution with channels
    eg of channel RGB image, what determines
    the colours
    """

    kh, kw, kc = kernel.shape
    m, h, w, c = images.shape
    sh, sw = stride
    if padding == 'same':
        ph = int(((h - 1) * sh + kh - h) / 2) + 1
        pw = int(((w - 1) * sw + kw - w) / 2) + 1
    elif padding == 'valid':
        ph = 0
        pw = 0
    else:
        ph, pw = padding
    padded = np.pad(images, ((0, 0), (ph, ph), (pw, pw), (0, 0)), 'constant')
    ch = int((h + 2 * ph - kh) / sh) + 1
    cw = int((w + 2 * pw - kw) / sw) + 1
    convolved_images = np.zeros((m, ch, cw))
    for i in range(ch):
        for j in range(cw):
            convolved_images[:, i, j] = np.sum(
                padded[:, i * sh: i * sh + kh, j * sw: j * sw + kw, :]
                * kernel, axis=(1, 2, 3))
    return convolved_images
