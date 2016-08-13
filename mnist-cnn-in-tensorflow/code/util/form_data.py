# -*- coding: utf-8 -*-
#
#

import gzip
import numpy as np
import settings.parameters as p


def extract_data(filename, num_images):
    """Extract the images into a 4D tensor [image index, y, x, channels].
    For MNIST data, the number of channels is always 1.
    Values are rescaled from [0, 255] down to [-0.5, 0.5].
    """
    print 'Extracting', filename
    with gzip.open(filename) as bytestream:
        # Skip the magic number and dimensions; we know these values.
        bytestream.read(16)

        buf = bytestream.read(p.IMAGE_SIZE * p.IMAGE_SIZE * num_images)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = (data - (p.PIXEL_DEPTH / 2.0)) / p.PIXEL_DEPTH
        data = data.reshape(num_images, p.IMAGE_SIZE, p.IMAGE_SIZE, 1)
        return data
