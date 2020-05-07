from NDOCD.load_data import get_amazon_graph
from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from time import time
from NDOCD.load_data import write_communities_to_file
from NDOCD.measures import normalized_mutual_information

# graph = get_amazon_graph()
# save_npz("data/amazon/graph.npz", graph)
graph = load_npz("data/amazon/graph.npz")
# ndocd = NDOCD(graph)
# np.save("data/amazon/neighbours.npy", ndocd.neighbours_edges)
ndocd = NDOCD(graph, np.load("data/amazon/neighbours.npy"))

ndocd.JS_threshold = 0.5
ndocd.MD_threshold = 0.5

# com = ndocd.initialize_new_community()
# com = ndocd.algorithm_step2(com)
# print(np.sum(com.vertices.toarray()))
# com = ndocd.create_new_community()

coms = ndocd.find_all_communities()
file = "data/amazon/coms"
write_communities_to_file(coms, file)
normalized_mutual_information(file, "data/amazon/com-amazon.all.dedup.cmty.txt")
