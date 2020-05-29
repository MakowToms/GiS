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
modification_number = 20
modification_percent = 0.2
for modification, modification_type in zip([False, True, True], ["percent", "percent", "number"]):
    this_times = []
    this_nmis = []
    this_mods = []
    this_ncoms = []
    this_mods_base = []
    this_coms_base = []
    for N in N_list:
        time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b2_" + str(N), MD_threshold=0.3, JS_threshold=0.3, modification=modification, modification_type=modification_type, modification_number=modification_number, modification_percent=modification_percent)
        this_times.append(time)
        this_nmis.append(nmi)
        this_mods.append(mod_ndocd)
        this_ncoms.append(n_coms)
        this_mods_base.append(mod_base)
        this_coms_base.append(n_coms_base)
        print(f'Ended: N - {N}, time - {time} \n')
    times.append(this_times)
    nmis.append(this_nmis)
    modularities.append(this_mods)
    n_communities.append(this_ncoms)
    labels.append(f"N = {N}")
    modularities_base.append(this_mods_base)
    n_communities_base.append(this_coms_base)
    print(f'\n\n Ended: modification, modification_type - {modification, modification_type} \n\n')


labels = ["Base NDOCD", "Modification percent", "Modification number", "BigClam"]
plot_measure_results_data(times, log_y=True, x=N_list, labels=labels, title_base="Time for different number of vertices", title_ending="", ylabel="Time [s]", xlabel="Number of vertices", save_name="plots/b1z1_time")

import pandas as pd
times[3] = list(pd.read_csv("time.csv", header=None).iloc[:, 1]*10)

pickle.dump(times, open("time.pickle", 'wb'))
