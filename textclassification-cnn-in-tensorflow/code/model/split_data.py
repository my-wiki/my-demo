# -*- coding: utf-8 -*-
"""Split the Original Dataset to Training Part and Test Part.
"""

import numpy as np
import settings.parameters as sp


def split_data(x, y):
    np.random.seed(sp.RANDOM_SEED)
    shuffle_indices = np.random.permutation(np.arange(len(y)))
    x_shuffled = x[shuffle_indices]
    y_shuffled = y[shuffle_indices]
    # Split train/test set
    x_train, x_dev = x_shuffled[:-1000], x_shuffled[-1000:]
    y_train, y_dev = y_shuffled[:-1000], y_shuffled[-1000:]
    return x_train, x_dev, y_train, y_dev


def cross_validation():
    pass
