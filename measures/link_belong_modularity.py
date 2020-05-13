'''
Code copied from:
https://github.com/RapidsAtHKUST/CommunityDetectionCodes/tree/master/Metrics/metrics
Only to research cases
'''

import networkx as nx
import numpy as np
import math
from functools import reduce
import re


class FuncTag:
    def __init__(self):
        pass

    exp_inv_mul_tag = 'exp_inv_mul'
    mul_tag = 'mul'
    min_tag = 'min'
    max_tag = 'max'


def get_graph_info(file_path):
    def extract_first_two(collection):
        splited = collection.split()
        return [int(splited[0]), int(splited[1])]

    with open(file_path) as ifs:
        lines = map(lambda ele: ele.strip(), ifs.readlines())
        lines = filter(lambda ele: not ele.startswith('#') and re.match('.*[0-9]+.*[0-9]+', ele), lines)
        pair_list = []
        for element in list(lines):
            pair_list.append(extract_first_two(element))
        return nx.Graph(pair_list)


def get_coefficient_func(tag):
    if tag == FuncTag.exp_inv_mul_tag:
        return lambda l, r: 1.0 / reduce(lambda il, ir: il * ir, map(lambda ele: 1.0 + math.exp(2 - ele), [l, r]), 1)
    elif tag == FuncTag.mul_tag:
        return lambda l, r: l * r
    elif tag == FuncTag.min_tag:
        return min
    elif tag == FuncTag.max_tag:
        return max


def cal_modularity(input_graph, comm_result):
    return LinkBelongModularity(input_graph, comm_result,
                                get_coefficient_func(FuncTag.exp_inv_mul_tag)).calculate_modularity()


class LinkBelongModularity:
    PRECISION = 0.0001

    def __init__(self, input_graph, comm_result, coefficient_func):
        """
        :type input_graph: nx.Graph
        """
        self.comm_list = comm_result
        self.graph = input_graph
        self.coefficient_func = coefficient_func
        self.belong_weight_dict = {}
        self.in_degree_dict = {}
        self.out_degree_dict = {}

        def init_belong_weight_dict():
            belong_dict = {}
            for comm in comm_result:
                for mem in comm:
                    if mem not in belong_dict:
                        belong_dict[mem] = 0
                    belong_dict[mem] += 1
            for mem in belong_dict:
                self.belong_weight_dict[mem] = 1.0 / belong_dict[mem] if belong_dict[mem] != 0 else 0

        def init_degree_dicts():
            for vertex in self.graph.nodes():
                # since graph here studied are used in undirected manner
                self.in_degree_dict[vertex] = self.graph.degree(vertex)
                self.out_degree_dict[vertex] = self.graph.degree(vertex)
            return

        init_belong_weight_dict()
        init_degree_dicts()

    def calculate_modularity(self):
        modularity_val = 0
        vertex_num = self.graph.number_of_nodes()
        edge_num = self.graph.number_of_edges()
        for comm in self.comm_list:
            comm_size = len(comm)
            f_val_matrix = np.ndarray(shape=(comm_size, comm_size), dtype=float)
            f_val_matrix.fill(0)
            f_sum_in_vec = np.zeros(comm_size, dtype=float)
            f_sum_out_vec = np.zeros(comm_size, dtype=float)
            in_deg_vec = np.zeros(comm_size, dtype=float)
            out_deg_vec = np.zeros(comm_size, dtype=float)

            # calculate f_val_matrix, f_sum_in, f_sum_out
            for i in range(comm_size):
                src_mem = comm[i]
                in_deg_vec[i] = self.in_degree_dict[src_mem]
                out_deg_vec[i] = self.out_degree_dict[src_mem]
                for j in range(comm_size):
                    dst_mem = comm[j]
                    if i != j and self.graph.has_edge(src_mem, dst_mem):
                        f_val_matrix[i][j] = self.coefficient_func(self.belong_weight_dict[src_mem],
                                                                   self.belong_weight_dict[dst_mem])
                        f_sum_out_vec[i] += f_val_matrix[i][j]
                        f_sum_in_vec[j] += f_val_matrix[i][j]

            f_sum_in_vec /= vertex_num
            f_sum_out_vec /= vertex_num

            for i in range(comm_size):
                for j in range(comm_size):
                    if i != j and f_val_matrix[i][j] > LinkBelongModularity.PRECISION:
                        null_model_val = out_deg_vec[i] * in_deg_vec[j] * f_sum_out_vec[i] * f_sum_in_vec[j] / edge_num
                        modularity_val += f_val_matrix[i][j] - null_model_val
        modularity_val /= edge_num
        return modularity_val


if __name__ == '__main__':
    graph = get_graph_info('data/email/email-Eu-core.txt')
    graph.edges
    print(cal_modularity(get_graph_info('data/demo_graph.csv'), [[0, 1, 5], [1, 2, 3, 4, 7, 8]]))
    my_graph = [[0, 1], [1, 2], [0, 2], [3, 4], [4, 5], [3, 5], [13, 14], [14, 15], [13, 15], [3, 13]]
    communities = [[0, 1, 2], [3, 4, 5], [13, 14, 15]]
    print(cal_modularity(nx.Graph(my_graph), communities))
    print(cal_modularity(nx.Graph(my_graph), [communities[0]]))

