from NDOCD.load_data import get_email_graph
from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from time import time
from NDOCD.load_data import write_communities_to_file
from NDOCD.measures import normalized_mutual_information

# graph = get_email_graph()
# save_npz("data/email/graph.npz", graph)
graph = load_npz("data/email/graph.npz")
# ndocd = NDOCD(graph)
# np.save("data/email/neighbours.npy", ndocd.neighbours_edges)
ndocd = NDOCD(graph, np.load("data/email/neighbours.npy"))

ndocd.JS_threshold = 0.2
ndocd.MD_threshold = 0.25

# com = ndocd.initialize_new_community()
# com = ndocd.algorithm_step2(com)
# print(np.sum(com.vertices.toarray()))
# com = ndocd.create_new_community()

coms = ndocd.find_all_communities(prune_every=1)
file = "data/email/coms"
write_communities_to_file(coms, file)
normalized_mutual_information(file, "data/email/email-communities.txt")

ndocd.graph
graph
len(coms)


