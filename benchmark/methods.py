from scipy.sparse import load_npz, save_npz
from NDOCD.NDOCD import NDOCD
import numpy as np
from NDOCD.load_data import write_communities_to_file, get_benchmark_graph
from measures.mutual_information import normalized_mutual_information
from measures.link_belong_modularity import cal_modularity, get_graph_info
from benchmark.rewrite_communities import rewrite_communities, get_communities_list
import time
import subprocess
import re


def test_ndocd(folder, file_appending, bigger_than=6, weighted=False, **kwargs):
    graph = get_benchmark_graph(folder, file_appending, weighted=weighted)
    rewrite_communities(folder, file_appending)

    start = time.time()
    ndocd = NDOCD(graph, **kwargs)
    coms = ndocd.find_all_communities(prune_every=10)
    end = time.time()
    coms2 = [list(com.indices) for com in coms if len(list(com.indices)) > bigger_than]
    print(f'Found communities: {len(coms2)}')
    com_list = get_communities_list(folder, file_appending)
    print(f'Proper number of communities: {len(com_list)}')
    file = folder + "coms"
    write_communities_to_file([com for com in coms if len(list(com.indices)) > bigger_than], file)

    # one measure - normalized mutual information
    nmi = normalized_mutual_information(file, folder + "community" + file_appending + "-converted.dat")
    print(f'normalized_mutual_information {nmi:0.04}')

    # second measure - link belong modularity
    graph_info = get_graph_info(folder + "network" + file_appending + "-transformed.dat")
    mod_ndocd = cal_modularity(graph_info, coms2)
    mod_base = cal_modularity(graph_info, com_list)
    print(f'modularity for ndocd {mod_ndocd:0.04}')
    print(f'modularity for ground-truth {mod_base:0.04}')
    return end-start, nmi, mod_ndocd, mod_base, len(coms2), len(com_list)


def create_benchmark(N=500, degree=25, max_degree=50, mu=0.1, on_over_n=0.1, om=2, file_appending="500"):
    on = int(N*on_over_n)
    text = f'-N {N} \n-k {degree} \n-maxk {max_degree} \n-mu {mu} \n-t1 2 \n-t2 1 \n-minc 10 \n-maxc 50 \n-on {on} \n-om {om}'
    with open('LFR-Benchmark/binary_networks/flags.dat', 'w') as f:
        f.write(text)
    res = subprocess.check_output(['LFR-Benchmark/binary_networks/benchmark', '-f', 'LFR-Benchmark/binary_networks/flags.dat'])
    print(res)
    subprocess.check_call(['mv', 'network.dat', 'data/benchmark/network' + file_appending + '.dat'])
    subprocess.check_call(['mv', 'community.dat', 'data/benchmark/community' + file_appending + '.dat'])


def create_benchmark_weighted(N=500, degree=25, max_degree=50, mut=0.2, muw=0.3, beta=1.5, on_over_n=0.1, om=2, file_appending="500"):
    on = int(N*on_over_n)
    text = f'-N {N} \n-k {degree} \n-maxk {max_degree} \n-mut {mut} \n-muw {muw} \n-beta {beta} \n-t1 2 \n-t2 1 \n-minc 10 \n-maxc 50 \n-on {on} \n-om {om}'
    with open('LFR-Benchmark/weighted_networks/flags.dat', 'w') as f:
        f.write(text)
    res = subprocess.check_output(['LFR-Benchmark/weighted_networks/benchmark', '-f', 'LFR-Benchmark/weighted_networks/flags.dat'])
    print(res)
    subprocess.check_call(['mv', 'network.dat', 'data/benchmark_weighted/network' + file_appending + '.dat'])
    subprocess.check_call(['mv', 'community.dat', 'data/benchmark_weighted/community' + file_appending + '.dat'])

