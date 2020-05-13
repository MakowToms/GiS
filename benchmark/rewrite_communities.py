

def create_communities(filename="LFR-Benchmark/binary_networks/community.dat"):
    communities = dict()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split("\t")
            vertex_number = int(line[0])
            for vertex in line[1].split(" ")[:-1]:
                vertex = int(vertex)
                old_community = communities.get(vertex)
                if old_community is None:
                    old_community = []
                old_community.append(vertex_number)
                communities[vertex] = old_community
    with open(filename.replace(".dat", "-converted.dat"), 'w') as f:
        for key in sorted(list(communities.keys())):
            f.write(str(communities[key]).replace(", ", " ")[1:-1] + '\n')
