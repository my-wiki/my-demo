# -*- coding: utf-8 -*-
#
#

import gzip
import numpy as np
import settings.parameters as p


def extract_labels(filename, num_images):
    """Extract the labels into a 1-hot matrix [image index, label index]."""
    print 'Extracting', filename
    with gzip.open(filename) as bytestream:
        # Skip the magic number and count; we know these values.
        bytestream.read(8)

        buf = bytestream.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8)
    # Convert to dense 1-hot representation.
    return (np.arange(p.NUM_LABELS) == labels[:, None]).astype(np.float32)
