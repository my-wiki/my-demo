# -*- coding: utf-8 -*-
"""Some functions to read and write file.
"""


def read_from_text(path):
    with open(path, "rb") as f:
        return f.readlines()
