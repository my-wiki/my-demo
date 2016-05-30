# -*- coding: utf-8 -*-
#
#
NUM_LABELS = 10
IMAGE_SIZE = 28
PIXEL_DEPTH = 255
VALIDATION_SIZE = 5000
WORK_DIRECTORY = "../data/mnist-data/"
SOURCE_URL = 'http://yann.lecun.com/exdb/mnist/'
# We'll bundle groups of examples during training for efficiency.
# This defines the size of the batch.
BATCH_SIZE = 60
# We have only one channel in our grayscale images.
NUM_CHANNELS = 1
# The random seed that defines initialization.
SEED = 42
