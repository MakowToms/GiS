

def rewrite_communities(filename="LFR-Benchmark/binary_networks/community.dat"):
    communities = get_communities_dict(filename)
    with open(filename.replace(".dat", "-converted.dat"), 'w') as f:
        for key in sorted(list(communities.keys())):
            f.write(str(communities[key]).replace(", ", " ")[1:-1] + '\n')


def get_communities_dict(filename="LFR-Benchmark/binary_networks/community.dat"):
    communities = dict()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\t")
            vertex_number = int(line[0]) - 1
            for vertex in line[1].split(" ")[:-1]:
                vertex = int(vertex)
                old_community = communities.get(vertex)
                if old_community is None:
                    old_community = []
                old_community.append(vertex_number)
                communities[vertex] = old_community
    return communities


def get_communities_list(filename="LFR-Benchmark/binary_networks/community.dat"):
    communities = get_communities_dict(filename)
    coms = []
    for key in sorted(list(communities.keys())):
        coms.append(communities[key])
    return coms
