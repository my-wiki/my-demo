# -*- coding: utf-8 -*-
import numpy as np


class AdjacencyList(object):
    """Calculate an adjacency list for a given array of an adjacency matrix.
    """
    def get_adjacency_list(self, adjacency_matrix):
        list = []

        for i in xrange(len(adjacency_matrix)):
            v = [j for j in xrange(len(adjacency_matrix[i])) if adjacency_matrix[i][j]]
            list.append(v)
        return list
