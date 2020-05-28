from scipy.sparse import load_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info

# graph = get_email_graph()
# save_npz("data/email/graph.npz", graph)
graph = load_npz("data/email/graph.npz")
# ndocd = NDOCD(graph)
# np.save("data/email/neighbours.npy", ndocd.neighbours_edges)
ndocd = NDOCD(graph, np.load("data/email/neighbours.npy"), modification=True)

ndocd.JS_threshold = 0.2
ndocd.MD_threshold = 0.3

# com = ndocd.initialize_new_community()
# com = ndocd.algorithm_step2(com)
# print(np.sum(com.vertices.toarray()))
# com = ndocd.create_new_community()

coms = ndocd.find_all_communities(prune_every=1)
bigger_than = 1
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]
len(coms2)
file = "data/email/coms"
write_communities_to_file(coms[:10], file)
normalized_mutual_information(file, "data/email/email-communities")

cal_modularity(get_graph_info("data/email/email-transformed.txt"), coms2[:10])

ndocd.graph
graph
len(coms)


