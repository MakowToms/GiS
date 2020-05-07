from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np
from NDOCD.Community import Community
from operator import itemgetter
from time import time


class NDOCD:
    def __init__(self, graph, neighbours_edges=None, beta=0.3, MD_threshold=0.2, JS_threshold=0.2):
        self.graph = graph
        self.n = graph.shape[0]
        self.beta = beta
        self.degrees = self.compute_degrees()
        print("degrees created")
        if neighbours_edges is not None:
            self.neighbours_edges = neighbours_edges
        else:
            self.neighbours_edges = self.compute_neighbours_edges()
        self.MD_threshold = MD_threshold
        self.JS_threshold = JS_threshold

    def compute_degrees(self):
        degrees = self.sum_of_rows(self.graph)
        degrees[degrees<2] = 2
        return degrees

    def update_degrees(self, community):
        self.degrees -= self.sum_of_rows(community.get_graph())
        self.degrees[self.degrees<2] = 2

    @staticmethod
    def sum_of_rows(csr):
        return np.array(np.sum(csr, axis=1))[:, 0]

    def compute_neighbours_edges(self):
        '''
        return doubled neighbourhood edges parameter
        :return:
        '''
        neighbours_edges = np.zeros([self.n])
        for i in range(self.n):
            neighbours_edges[i] = self.compute_neighbours_for_vertex(i)
        return neighbours_edges

    def remove_neighbours_edges(self, community):
        for i in community.get_vertex_indices():
            for j in self.graph[i].indices:
                edges = self.multiply_sparse(community.get_graph()[i], self.graph[j], create_mask=True)
                if edges.shape[0] == 0:
                    edges = 0
                self.neighbours_edges[j] -= edges

    def compute_neighbours_edges_from_beginning_for_vertexes_with_removed_edges(self, community):
        for i in community.get_vertex_indices():
            self.neighbours_edges[i] = self.compute_neighbours_for_vertex(i)

    def compute_neighbours_for_vertex(self, i):
        all_edges = 0
        mask = self.create_true_false_mask(self.graph[i])
        for j in self.graph[i].indices:
            edges = self.multiply_sparse(self.graph[j], mask)
            if edges.shape[0] == 0:
                edges = 0
            all_edges += edges
        return all_edges

    def compute_clustering_coefficient(self):
        return self.neighbours_edges / (self.degrees * (self.degrees - 1))

    def compute_CNFV(self):
        return self.beta * self.compute_clustering_coefficient() + (1 - self.beta) * self.degrees / self.n

    def get_max_CNFV_vertex(self):
        return np.argmax(self.compute_CNFV())

    def initialize_new_community(self):
        initial_vertex = self.get_max_CNFV_vertex()
        community = Community(self.n, initial_vertex)
        for index, degree in self.get_neighbour_vertices(initial_vertex):
            if self.can_add_to_clique(index, community):
                community.add_vertex(index, self.graph[index])
        return community

    def get_neighbour_vertices(self, vertex):
        neighbours = self.graph[vertex].indices
        neighbour_degrees = []
        for j in neighbours:
            neighbour_degrees.append((j, self.degrees[j]))
        neighbour_degrees.sort(key=itemgetter(1), reverse=True)
        return neighbour_degrees

    def can_add_to_clique(self, index, community):
        need_to_contain = community.get_vertex_indices()
        container = self.graph[index].indices
        return np.all(np.isin(need_to_contain, container))

# step 2 of algorithm

    def community_neighbours(self, community):
        vertexes = community.get_vertex_indices()
        neighbours = self.graph[vertexes[0]]
        for vertex in vertexes[1:]:
            neighbours += self.graph[vertex]
        # remove actual community members
        neighbours[:, vertexes] = 0
        return neighbours.nonzero()[1]

    def edges_between_community_and_vertices(self, community, vertices):
        return (vertices * community.get_vertices().transpose()).toarray()

    def can_add_to_community(self, community):
        neighbours_indices = self.community_neighbours(community)
        if neighbours_indices.shape[0] == 0:
            return neighbours_indices
        neighbours_graph = self.graph[neighbours_indices]
        M_iK = self.edges_between_community_and_vertices(community, neighbours_graph).transpose()
        JS = M_iK / community.get_edges_number()
        MD = M_iK / self.degrees[neighbours_indices]
        vertices_to_add = np.logical_or(JS > self.JS_threshold, MD > self.MD_threshold)
        vertices_to_add = np.array(vertices_to_add)[0, :]
        return neighbours_indices[vertices_to_add]

    def algorithm_step2(self, community):
        while True:
            vertices_to_add = self.can_add_to_community(community)
            if vertices_to_add.shape[0] == 0:
                break
            for vertex in vertices_to_add:
                community.add_vertex(vertex, self.graph[vertex])
        return community

    def create_new_community(self, prune=False):
        community = self.initialize_new_community()
        self.algorithm_step2(community)
        community.stop_adding_vertices()
        self.update_degrees(community)
        self.remove_neighbours_edges(community)
        self.graph = self.graph - community.get_graph()
        self.graph.eliminate_zeros()
        if prune:
            self.graph.prune()
        self.compute_neighbours_edges_from_beginning_for_vertexes_with_removed_edges(community)
        return community

    def find_all_communities(self, prune_every=100):
        communities = []
        prune_counter = 0
        mean_community_size = 0
        start = time()
        while not np.all(self.degrees == 2):
        # for i in range(1000):
            community = self.create_new_community()
            communities.append(community.get_vertices())
            prune_counter += 1
            mean_community_size += community.n_vertices
            if prune_counter == prune_every:
                prune_counter = 0
                self.graph.prune()
                print("Time: ", time() - start, " Mean community size: ", mean_community_size / prune_every)
                mean_community_size = 0
        return communities

    @staticmethod
    def create_true_false_mask(vertex, as_column=True):
        '''
        :param vertex: scipy sparse row
        :param as_column: if should transpose
        :return: mask as a column
        '''
        vertex = (vertex != 0)
        if as_column:
            return vertex.transpose()
        else:
            return vertex

    @staticmethod
    def multiply_sparse(row, column, create_mask=False, get_data=True):
        if create_mask:
            column = NDOCD.create_true_false_mask(column)
        if get_data:
            return (row @ column).data
        else:
            return row @ column
