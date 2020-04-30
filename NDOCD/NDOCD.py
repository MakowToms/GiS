from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np


class NDOCD:
    def __init__(self, graph):
        self.graph = graph
        self.n = graph.shape[0]
        self.degrees = self.compute_degrees()
        self.neighbours_edges = self.compute_neighbours_edges()

    def compute_degrees(self):
        return np.sum(self.graph, axis=0)

    def update_degrees(self, community):
        self.degrees -= np.sum(community.get_graph(), axis=0)

    def compute_neighbours_edges(self):
        '''
        return doubled neighbourhood edges parameter
        :return:
        '''
        neighbours_edges = np.zeros([self.n])
        for i in range(self.n):
            mask = (self.graph[i] != 0).transpose()
            for j in self.graph[i].indices:
                neighbours_edges[i] += (self.graph[j] @ mask).data
        return neighbours_edges

    def update_neighbours_edges(self, community):
        # for i
        pass

