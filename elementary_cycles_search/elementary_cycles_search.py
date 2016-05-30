# -*- coding: utf-8 -*-
import numpy as np
from adjacency_list import AdjacencyList
from strong_connected_components import StrongConnectedComponents


class ElementaryCyclesSearch(object):
    """Search all elementary cycles in a given directed graph.
    It requires:
        an list of the objects representing the nodes,
        an adjacency-matrix of type boolean.
    It then calculate elementary cycles based on the adjacency-matrix,
        and returns a list of lists (represents an elementary cycle.)
    The algorithm is based on the search for strong connected components
        in a graph.
    """
    def __init__(self, matrix, graphnodes):
        # List of cycles
        self.__cycles = None
        # Adjacency-list of graph
        self.__adj_list = AdjacencyList().get_adjacency_list(matrix)
        # graph nodes
        self.__graph_nodes = graphnodes
        # blocked nodes, used by Johnson
        self.__blocked = None
        # B-lists
        self.__B = None
        # Stack for nodes
        self.__stack = None

    def get_elementary_cycles(self):

        self.__cycles = []
        self.__blocked = np.zeros(len(self.__adj_list), dtype=bool)
        self.__B = np.zeros(len(self.__adj_list))
        self.__stack = []

        sccs = StrongConnectedComponents(self.__adj_list)
        s = 0

        while True:
            scc_result = sccs.get_adjacency_list(s)
            if scc_result and scc_result.get_adj_list:
                scc = scc_result.get_adj_list()
                s = scc_result.get_lowest_nodeId()

                for j in xrange(len(scc)):
                    if scc[j] and len(scc[j]) > 0:
                        self.__blocked[j] = False
                        self.__B[j] = []
                self.__find_cycles(s, s, scc)
                s += 1
            else:
                break
        return self.__cycles

    def __find_cycles(self, v, s, adj_list):
        """Calculates the cycles containing a given node in a strongly connected
            component. The method calls itself recursivly.
        """
        f = False
        self.__stack.append(v)
        self.__blocked[v] = True

        for i in xrange(len(adj_list)):
            w = adj_list[v][i]
            # found cycle
            if w == s:
                cycle = []
                for j in xrange(len(self.__stack)):
                    index = self.__stack[j]
                    cycle.append(self.__graph_nodes[index])
                self.__cycles.append(cycle)
                f = True
            elif self.__blocked[w]:
                if self.__find_cycles(w, s, adj_list):
                    f = True
        if f:
            self.__unblock(v)
        else:
            for i in xrange(len(adj_list)):
                w = adj_list[v][i]
                if v not in self.__B[w]:
                    self.__B[w].append(v)
        self.__stack.pop()
        return f

    def __unblock(self, node):
        """Unblocks recursivly all blocked nodes, starting wit ha given node.
        """
        self.__blocked[node] = False
        b_node = self.__B[node]
        while len(b_node) > 0:
            w = b_node[0]
            b_node = b_node[1:]
            if self.__blocked[w]:
                self.__unblock(w)
