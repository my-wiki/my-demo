# -*- coding: utf-8 -*-
#
import numpy as np
from elementary_cycles_search import ElementaryCyclesSearch


def debug():
    nodes = ["Node " + str(i) for i in xrange(10)]

    adj_matrix = np.zeros(shape=(10, 10), dtype=bool)
    adj_matrix[0][1] = True
    adj_matrix[1][2] = True
    adj_matrix[2][0] = True
    adj_matrix[2][6] = True
    adj_matrix[3][4] = True
    adj_matrix[4][5] = True
    adj_matrix[4][6] = True
    adj_matrix[5][3] = True

    adj_matrix[6][7] = True
    adj_matrix[7][8] = True
    adj_matrix[8][6] = True
    adj_matrix[6][1] = True

    ecs = ElementaryCyclesSearch(adj_matrix, nodes)
    cycles = ecs.get_elementary_cycles()

    for i in xrange(len(cycles)):
        cycle = cycles[i]
        for j in xrange(len(cycle)):
            node = cycle[j]
            if j < len(cycle) - 1:
                print str(node) + " --> "
            else:
                print node
        print "\n"

if __name__ == '__main__':
    debug()
