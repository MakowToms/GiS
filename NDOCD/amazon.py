from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_communities_list2, get_amazon_graph
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info
import time
from measures.modularity import convert_communities_to_dict, get_modularity

# graph = get_amazon_graph()
# save_npz("data/amazon/graph.npz", graph)
graph = load_npz("data/amazon/graph.npz")
start = time.time()
ndocd = NDOCD(graph, modification=True, modification_type="percent", modification_percent=0.2)

ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.3

coms = ndocd.find_all_communities()
end = time.time()

bigger_than = 6
file = "data/amazon/coms"
write_communities_to_file([com for com in coms if len(list(com.indices)) > bigger_than], file)
nmi = normalized_mutual_information(file, "data/amazon/communities")
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]

length = 0
for com in coms2:
    length += len(com)

mod_ndocd = get_modularity(get_graph_info("data/amazon/amazon-transformed.txt"), convert_communities_to_dict(coms2))
mod_base = get_modularity(get_graph_info("data/amazon/amazon-transformed.txt"), convert_communities_to_dict(get_communities_list2("data/amazon/communities", " ")))
print(f"Normalized mutual information: {nmi:0.04}")
print(f'Average size: {length/len(coms2)}')
print(f'Number of communities: {len(coms2)}')
print(f'Proper number of communities: {len(get_communities_list2("data/amazon/communities", " "))}')
print(f'Time: {end-start}')
print(f'modularity for ndocd {mod_ndocd:0.04}')
print(f'modularity for ground-truth {mod_base:0.04}')
