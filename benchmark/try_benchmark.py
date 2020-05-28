from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_benchmark_graph
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info
from benchmark.rewrite_communities import rewrite_communities, get_communities_list
import time

folder = "data/benchmark_weighted/"
file_appending = "b1_" + str(500) + str(0.2)
graph = get_benchmark_graph(folder, file_appending=file_appending, weighted=True)
rewrite_communities(folder, file_appending)
# # save_npz("data/benchmark/graph.npz", graph)
# # graph = load_npz("data/benchmark/graph.npz")
ndocd = NDOCD(graph)
# # np.save("data/benchmark/neighbours.npy", ndocd.neighbours_edges)
# # ndocd = NDOCD(graph, np.load("data/benchmark/neighbours.npy"), modification=True, modification_type="percent", modification_percent=0.5, modification_number=10)
#
ndocd.JS_threshold = 1
ndocd.MD_threshold = 1
#
coms = ndocd.find_all_communities(prune_every=1)
# bigger_than = 6
# coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]
# len(coms2)
# len(get_communities_list())
# file = "data/benchmark/coms"
# write_communities_to_file([com for com in coms if len(list(com.indices)) > bigger_than], file)
#
# # one measure - normalized mutual information
# nmi = normalized_mutual_information(file, "LFR-Benchmark/binary_networks/community-converted.dat")
# print(f'normalized_mutual_information {nmi:0.04}')
#
# # second measure - link belong modularity
# mod_ndocd = cal_modularity(get_graph_info("LFR-Benchmark/binary_networks/network-transformed.dat"), coms2)
# mod_base = cal_modularity(get_graph_info("LFR-Benchmark/binary_networks/network-transformed.dat"), get_communities_list())
# print(f'modularity for ndocd {mod_ndocd:0.04}')
# print(f'modularity for ground-truth {mod_base:0.04}')
