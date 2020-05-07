from NDOCD.NDOCD import NDOCD
from NDOCD.Community import Community
from NDOCD.load_data import random_graph, get_actors_graph
from scipy.sparse import save_npz, load_npz
import numpy as np

np.random.seed(123)
graph = random_graph(size=150, edges=1200)
ndocd = NDOCD(graph)
# ndocd.neighbours_edges
# ndocd.compute_neighbours_edges()
# com.get_graph().toarray()
# graph.toarray()
# ndocd.graph.toarray()
# graph = get_actors_graph()
# save_npz("data/actors_graph.npz", graph)
graph = load_npz("data/actors_graph.npz")
# np.save("data/actors_neighbours.npy", ndocd.neighbours_edges)

ndocd = NDOCD(graph, np.load("data/actors_neighbours.npy"))

# graph.toarray()
com = ndocd.initialize_new_community()
com.get_graph()[com.get_vertex_indices()].toarray()[:, com.get_vertex_indices()]

ndocd.JS_threshold = 0.18
ndocd.MD_threshold = 0.18

com = ndocd.initialize_new_community()
com = ndocd.algorithm_step2(com)
print(np.sum(com.vertices.toarray()))
# com = ndocd.create_new_community()

coms = ndocd.find_all_communities()
coms2 = ndocd.find_all_communities()
coms3 = ndocd.find_all_communities()
coms4 = ndocd.find_all_communities()
coms5 = ndocd.find_all_communities()
coms6 = ndocd.find_all_communities()
coms2

np.sum(ndocd.degrees) / ndocd.n
np.sum(ndocd.compute_degrees())

ndocd.compute_CNFV()
ndocd.get_max_CNFV_vertex()
ndocd.degrees[ndocd.get_max_CNFV_vertex()]
ndocd.compute_clustering_coefficient()[ndocd.get_max_CNFV_vertex()]
ndocd.neighbours_edges[ndocd.get_max_CNFV_vertex()]
ndocd.neighbours_edges[6534]
com.get_vertex_indices()
ndocd.graph[6534]
ndocd.neighbours_edges[np.argmax(ndocd.neighbours_edges)]
ndocd.degrees[np.argmax(ndocd.neighbours_edges)]
ndocd.graph[5771].indices
ndocd.graph[5168].indices
ndocd.graph[3953].indices
ndocd.graph[3629].indices

com.n_vertices
com.get_vertex_indices()
ndocd.n
neighbours_indices = ndocd.community_neighbours(com)
neighbours_graph = ndocd.graph[neighbours_indices]
neighbours_graph * com.get_vertices().transpose().toarray()
# community_vertices = ndocd.graph[com.get_vertex_indices()]
# mask = ndocd.create_true_false_mask(neighbours_graph)
# np.sum(ndocd.multiply_sparse(community_vertices, mask, get_data=False), axis=0)
M_iK = ndocd.edges_between_community_and_vertices(com, neighbours_graph)
JS = M_iK / com.get_edges_number()
MD = M_iK / ndocd.degrees[neighbours_indices]
vertices_to_add = np.logical_or(JS > 0.5, MD > 0.5)
vertices_to_add = np.array(vertices_to_add)[0, :]
neighbours_indices[vertices_to_add]
vertices_to_add = ndocd.can_add_to_community(com)

for vertex in vertices_to_add:
    print(vertex)
    com.add_vertex(vertex, ndocd.graph[vertex])

ndocd.degrees
ndocd.neighbours_edges

com = ndocd.create_new_community()
ndocd.neighbours_edges
ndocd.degrees
