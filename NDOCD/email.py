from scipy.sparse import load_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_email_graph, get_communities_list2
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info
import time

graph = get_email_graph()
start = time.time()
ndocd = NDOCD(graph)
# np.save("data/email/neighbours.npy", ndocd.neighbours_edges)
# ndocd = NDOCD(graph, np.load("data/email/neighbours.npy"), modification=True)

ndocd.JS_threshold = 0.33
ndocd.MD_threshold = 0.33

coms = ndocd.find_all_communities(prune_every=1)
end = time.time()

bigger_than = 6
file = "data/email/coms"
write_communities_to_file([com for com in coms if len(list(com.indices)) > bigger_than], file)
nmi = normalized_mutual_information(file, "data/email/email-communities")
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]

length = 0
for com in coms2:
    length += len(com)

mod_ndocd = cal_modularity(get_graph_info("data/email/email-transformed.txt"), coms2)
mod_base = cal_modularity(get_graph_info("data/email/email-transformed.txt"), get_communities_list2("data/email/email-communities", " "))
print(f"Normalized mutual information: {nmi:0.04}")
print(f'Average size: {length/len(coms2)}')
print(f'Number of communities: {len(coms2)}')
print(f'Proper number of communities: {len(get_communities_list2("data/email/email-communities", " "))}')
print(f'Time: {end-start}')
print(f'modularity for ndocd {mod_ndocd:0.04}')
print(f'modularity for ground-truth {mod_base:0.04}')
