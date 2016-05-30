# -*- coding: utf-8 -*-

import numpy as np
from scc_result import SccResult


class StrongConnectedComponents(object):
    """A helpclass for the search of all elementary cycles in a graph.
    It searches for strong connected components, using the algorithm of Tarjan.
    It requires an adjacency-list of a graph, and then:
        It gets a nodenumber s, for which it calculates the subgraph,containing
        all nodes {s,...,n} where n is the highest nodenumber in the original
        graph. (It builds a subgraph with all nodes with higher or same
        nodenumbers like the given node s.)
    It returns the strong connected component of this subgraph which contains
        the lowest nodenumber of all nodes in the subgraph.
    """
    def __init__(self, adj_list):
        # adjacency-list of original graph
        self.__adj_list_original = adj_list
        # Adjacency-list of currently viewed subgraph
        self.__adj_list = None
        # help attribute for finding scc's
        self.__visited = None
        # help attribute for finding scc's
        self.__stack = None
        # help attribute for finding scc's
        self.__lowlink = None
        # help attribute for finding scc's
        self.__number = None
        # help attribute for finding scc's
        self.__scc_counter = 0
        # help attribute for finding scc's
        self.__current_sccs = None

    def get_adjacency_list(self, node):
        self.__visited = np.zeros(len(self.__adj_list_original), dtype=bool)
        self.__lowlink = np.zeros(len(self.__adj_list_original), dtype=int)
        self.__number = np.zeros(len(self.__adj_list_original), dtype=int)
        self.__stack = []
        self.__current_sccs = []

        self.__make_adj_list_subgraph(node)

        for i in xrange(node, len(self.__adj_list_original)):
            print i
            print self.__visited[i]
            if not self.__visited[i]:
                self.__get_strong_connected_components(i)
                nodes = self.__get_lowestId_component()
                if nodes and (node not in nodes) and ((node + 1) not in nodes):
                    return self.get_adjacency_list(node + 1)
                else:
                    adjacency_list = self.__get_adj_list(nodes)
                    if adjacency_list:
                        for j in xrange(len(self.__adj_list_original)):
                            if len(adjacency_list[j]) > 0:
                                return SccResult(adjacency_list, j)
        return None

    def __make_adj_list_subgraph(self, node):
        """Builds the adjacency-list for a subgraph containing just nodes
            great than a given index
        """
        self.__adj_list = [[] for i in xrange(len(self.__adj_list_original))]

        for i in xrange(node, len(self.__adj_list_original)):
            successors = []
            for j in xrange(len(self.__adj_list_original[i])):
                if self.__adj_list_original[i][j] >= node:
                    successors.append(self.__adj_list_original[i][j])
            if len(successors) > 0:
                self.__adj_list[i] = successors
        print self.__adj_list

    def __get_lowestId_component(self):
        """calculate the strong connected component out of a set of scc's,
            that contains the node with the lowest index.
        """
        min_len = len(self.__adj_list)
        curr_scc = None

        for i in xrange(len(self.__current_sccs)):
            scc = self.__current_sccs[i]
            for j in xrange(len(scc)):
                if scc[j] < min_len:
                    curr_scc = scc
                    min_len = scc[j]
        return curr_scc

    def __get_adj_list(self, nodes):
        lowestId_adjacency_list = None

        if nodes:
            lowestId_adjacency_list = [[] for i in xrange(len(self.__adj_list))]
            for i in xrange(len(nodes)):
                node = nodes[i]
                for j in xrange(len(self.__adj_list[node])):
                    succ = self.__adj_list[node][j]
                    if succ in nodes:
                        lowestId_adjacency_list[node].append(succ)
        return lowestId_adjacency_list

    def __get_strong_connected_components(self, root):
        self.__scc_counter += 1
        self.__lowlink[root] = self.__scc_counter
        self.__number[root] = self.__scc_counter
        self.__visited[root] = True
        self.__stack.append(root)

        for i in xrange(len(self.__adj_list[root])):
            w = self.__adj_list[root][i]
            print "w1: " + str(w)
            if not self.__visited[w]:
                print "w2: " + str(w)
                self.__get_strong_connected_components(w)
                self.__lowlink[root] = min(self.__lowlink[root], self.__lowlink[w])
            elif self.__number[w] < self.__number[root]:
                if w in self.__stack:
                    self.__lowlink[root] = min(self.__lowlink[root], self.__number[w])

        # found scc
        if self.__lowlink[root] == self.__number[root] and len(self.__stack) > 0:
            next = -1
            scc = []

            while self.__number[next] > self.__number[root]:
                next = self.__stack.pop()
                scc.append(next)

            if len(scc) > 1:
                self.__current_sccs.append(scc)
