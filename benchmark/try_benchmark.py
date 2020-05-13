from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_benchmark_graph
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info
from benchmark.rewrite_communities import rewrite_communities, get_communities_list

graph = get_benchmark_graph()
rewrite_communities()
# save_npz("data/benchmark/graph.npz", graph)
# graph = load_npz("data/benchmark/graph.npz")
ndocd = NDOCD(graph)
# np.save("data/benchmark/neighbours.npy", ndocd.neighbours_edges)
# ndocd = NDOCD(graph, np.load("data/benchmark/neighbours.npy"))

ndocd.JS_threshold = 0.15
ndocd.MD_threshold = 0.25

# com = ndocd.initialize_new_community()
# com = ndocd.algorithm_step2(com)
# print(np.sum(com.vertices.toarray()))
# com = ndocd.create_new_community()

coms = ndocd.find_all_communities(prune_every=1)
bigger_than = 5
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]
len(coms2)
file = "data/benchmark/coms"
write_communities_to_file(coms, file)

# one measure - normalized mutual information
normalized_mutual_information(file, "LFR-Benchmark/binary_networks/community-converted.dat")

# second measure - link belong modularity
cal_modularity(get_graph_info("LFR-Benchmark/binary_networks/network-transformed.dat"), coms2)
cal_modularity(get_graph_info("LFR-Benchmark/binary_networks/network-transformed.dat"), get_communities_list())

