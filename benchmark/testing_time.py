from benchmark.methods import test_ndocd
from plots.plots import plot_measure_results_data
import pickle

folder = "data/benchmark/"
N_list = [i*200 for i in range(1, 11)]
times = []
nmis = []
modularities = []
n_communities = []
labels = []
modularities_base = []
n_communities_base = []
this_times = []
this_nmis = []
this_mods = []
this_ncoms = []
for N in N_list:
    time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N), MD_threshold=0.3, JS_threshold=0.3)
    this_times.append(time)
    this_nmis.append(nmi)
    this_mods.append(mod_ndocd)
    this_ncoms.append(n_coms)
    print(f'Ended: N - {N}, time - {time} \n')
times.append(this_times)
nmis.append(this_nmis)
modularities.append(this_mods)
n_communities.append(this_ncoms)
labels.append(f"N = {N}")
modularities_base.append(mod_base)
n_communities_base.append(n_coms_base)
print(f'\n\n Ended: N - {N} \n\n')


plot_measure_results_data(times, x=N_list, labels=labels, title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="JS and MD thresholds", save_name="plots/b1z1_time")
