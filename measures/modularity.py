from modularity_maximization.utils import get_modularity
from modularity_maximization import partition
from measures.link_belong_modularity import get_graph_info

# NXgraph = get_graph_info("data/benchmark/networkb1_100-transformed.dat")
# comm_dict = partition(NXgraph)
# max(comm_dict.values())
# max(comm_dict.items())
# len(comm_dict.items())
# sorted(comm_dict.items(), key=lambda item: item[0])
# comm_dict[0] = 1
# comm_dict[0] = [1, 2, 3, 4, 5, 6]
# for i in range(10):
#     comm_dict[i] = [1, 2, 3, 4, 5, 6]
# get_modularity(NXgraph, comm_dict)


def convert_communities_to_dict(coms):
    coms_dict = {}
    max_vertex = 0
    for index, com in enumerate(coms):
        for res in com:
            if res>max_vertex:
                max_vertex = res
            if coms_dict.__contains__(res):
                coms_dict[res].append(index + 1)
            else:
                coms_dict[res] = [index + 1]
    for item in coms_dict.items():
        if len(coms_dict[item[0]]) == 1:
            coms_dict[item[0]] = item[1][0]
    for i in range(max_vertex+1):
        if not coms_dict.__contains__(i):
            coms_dict[i] = []
    return coms_dict
