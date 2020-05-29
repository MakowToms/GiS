from scipy.sparse import load_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_actors_graph
from measures.link_belong_modularity import cal_modularity, get_graph_info
import time

graph = get_actors_graph()
start = time.time()
ndocd = NDOCD(graph)

ndocd.JS_threshold = 0.3
ndocd.MD_threshold = 0.3

coms = ndocd.find_all_communities()
end = time.time()

bigger_than = 6
coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]

length = 0
for com in coms2:
    length += len(com)

mod_ndocd = cal_modularity(get_graph_info("data/Filmweb Graph/actors-transformed.txt"), coms2)
print(f'Average size: {length/len(coms2)}')
print(f'Number of communities: {len(coms2)}')
print(f'Time: {end-start}')
print(f'modularity for ndocd {mod_ndocd:0.04}')

