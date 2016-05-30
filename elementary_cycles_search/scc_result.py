# -*- coding: utf-8 -*-


class SccResult(object):
    def __init__(self, adj_list, lowest_nodeId):
        self.__adj_list = adj_list
        self.__lowest_nodeId = lowest_nodeId
        self.__nodeId_of_Scc = set()
        if self.__adj_list:
            for i in xrange(self.__lowest_nodeId, len(self.__adj_list)):
                if len(self.__adj_list[i]) > 0:
                    self.__nodeId_of_Scc.add(i)

    def get_adj_list(self):
        return self.__adj_list

    def get_lowest_nodeId(self):
        return self.__lowest_nodeId
