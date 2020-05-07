from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix, dok_matrix
import numpy as np


class Community:
    def __init__(self, n, initial_vertex):
        self.n = n
        self.graph = dok_matrix((n, n))
        self.vertices = self.initial_vertices(initial_vertex)
        self.n_vertices = 1
        self.n_edges = 0
        self.is_csr = False

    def initial_vertices(self, initial_vertex):
        vertices = dok_matrix((1, self.n))
        vertices[0, initial_vertex] = 1
        return vertices

    def add_vertex(self, vertex, edges):
        self.n_vertices += 1
        self.vertices[0, vertex] = 1
        self.n_edges += np.sum(edges)
        non_zero_ind = self.vertices.nonzero()[1]
        edges = edges[:, non_zero_ind]
        self.graph[vertex, non_zero_ind] = edges
        self.graph[non_zero_ind, vertex] = edges

    def stop_adding_vertices(self):
        self.is_csr = True
        self.graph = self.graph.tocsr()
        self.vertices = self.vertices.tocsr()

    def get_graph(self):
        return self.graph

    def get_vertices(self):
        return self.vertices

    def get_vertex_indices(self):
        if self.is_csr:
            return self.vertices.indices
        else:
            return self.vertices.nonzero()[1]

    def get_edges_number(self):
        return self.n_edges
