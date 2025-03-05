#!/usr/bin/env python3
"""
This module has the method that performs
pooling on images
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    pooling on images
    c - no. of channels
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    # Calculate the output dimensions
    oh = int((h - kh) / sh) + 1
    ow = int((w - kw) / sw) + 1

    # Initialize the output tensor
    pooled_images = np.zeros((m, oh, ow, c))

    for i in range(oh):
        for j in range(ow):
            # Extract a patch from the image
            patch = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]

            # Apply pooling based on the specified mode
            if mode == 'max':
                pooled_patch = np.max(patch, axis=(1, 2))
            elif mode == 'avg':
                pooled_patch = np.mean(patch, axis=(1, 2))
            else:
                raise ValueError("Invalid pooling mode. Use 'max' or 'avg'.")

            # Store the pooled patch in the output
            pooled_images[:, i, j, :] = pooled_patch

    return pooled_images
