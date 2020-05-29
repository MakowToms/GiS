from scipy.sparse import load_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_actors_graph
from measures.link_belong_modularity import cal_modularity, get_graph_info
import time
from measures.modularity import convert_communities_to_dict, get_modularity

graph = get_actors_graph()
start = time.time()
# ndocd = NDOCD(graph)
# ndocd = NDOCD(graph, modification=True, modification_type="percent", modification_percent=0.2)
ndocd = NDOCD(graph, modification=True, modification_type="number", modification_number=20)

ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.3

coms = ndocd.find_all_communities(prune_every=10)
end = time.time()

bigger_than = 6
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]

length = 0
for com in coms2:
    length += len(com)

coms3 = convert_communities_to_dict(coms2)
# coms3[6956] = []
mod_ndocd = get_modularity(get_graph_info("data/Filmweb Graph/actors-transformed.txt"), coms3)
print(f'Average size: {length/len(coms2)}')
print(f'Number of communities: {len(coms2)}')
print(f'Time: {end-start}')
print(f'modularity for ndocd {mod_ndocd:0.04}')
