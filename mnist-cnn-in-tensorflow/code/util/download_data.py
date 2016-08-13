# -*- coding: utf-8 -*-
#
#
import os
import urllib
import settings.parameters as p


def maybe_download(filename):
    """A helper to download the data files if not present."""
    if not os.path.exists(p.WORK_DIRECTORY):
        os.mkdir(p.WORK_DIRECTORY)
    filepath = os.path.join(p.WORK_DIRECTORY, filename)
    if not os.path.exists(filepath):
        filepath, _ = urllib.urlretrieve(p.SOURCE_URL + filename, filepath)
        statinfo = os.stat(filepath)
        print 'Succesfully downloaded', filename, statinfo.st_size, 'bytes.'
    else:
        print 'Already downloaded', filename
    return filepath
