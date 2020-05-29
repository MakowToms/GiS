from benchmark.methods import test_ndocd
from plots.plots import plot_measure_results_data, create_8_plots
import pickle

folder = "data/benchmark/"
N_list = [500, 1000]
mu_list = [0.1, 0.2]
on_over_n_list = [0.1, 0.2]
times = []
nmis = []
modularities = []
n_communities = []
labels = []
modularities_base = []
n_communities_base = []
JS_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9]
MD_thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9]
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            this_times = []
            this_nmis = []
            this_mods = []
            this_ncoms = []
            for JS_threshold, MD_threshold in zip(JS_thresholds, MD_thresholds):
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b3_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
                this_times.append(time)
                this_nmis.append(nmi)
                this_mods.append(mod_ndocd)
                this_ncoms.append(n_coms)
                print(f'Ended: JS_threshold - {JS_threshold}, N - {N}, time - {time} \n')
            times.append(this_times)
            nmis.append(this_nmis)
            modularities.append(this_mods)
            n_communities.append(this_ncoms)
            labels.append(f"N = {N}, mu = {mu} on = {int(N*on_over_n)}")
            modularities_base.append(mod_base)
            n_communities_base.append(n_coms_base)
            print(f'\n\n Ended: N - {N} \n\n')


pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds), open("data/benchmark/b3z", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds = pickle.load(open("data/benchmark/b3z", 'rb'))
create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, JS_thresholds, "JS and MD thresholds", "b3z")


times = []
nmis = []
modularities = []
n_communities = []
labels = []
modularities_base = []
n_communities_base = []
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            MD_threshold = 0.3
            this_times = []
            this_nmis = []
            this_mods = []
            this_ncoms = []
            for JS_threshold in JS_thresholds:
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b3_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
                this_times.append(time)
                this_nmis.append(nmi)
                this_mods.append(mod_ndocd)
                this_ncoms.append(n_coms)
                print(f'Ended: JS_threshold - {JS_threshold}, N - {N}, time - {time} \n')
            times.append(this_times)
            nmis.append(this_nmis)
            modularities.append(this_mods)
            n_communities.append(this_ncoms)
            labels.append(f"N = {N}, mu = {mu} on = {int(N*on_over_n)}")
            modularities_base.append(mod_base)
            n_communities_base.append(n_coms_base)
            print(f'\n\n Ended: N - {N} \n\n')


pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds), open("data/benchmark/b3a", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds = pickle.load(open("data/benchmark/b3a", 'rb'))
create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, JS_thresholds, "JS thresholds", "b3a")

times = []
nmis = []
modularities = []
n_communities = []
labels = []
modularities_base = []
n_communities_base = []
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            JS_threshold = 0.3
            this_times = []
            this_nmis = []
            this_mods = []
            this_ncoms = []
            for MD_threshold in MD_thresholds:
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b3_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
                this_times.append(time)
                this_nmis.append(nmi)
                this_mods.append(mod_ndocd)
                this_ncoms.append(n_coms)
                print(f'Ended: MD_threshold - {MD_threshold}, N - {N}, time - {time} \n')
            times.append(this_times)
            nmis.append(this_nmis)
            modularities.append(this_mods)
            n_communities.append(this_ncoms)
            labels.append(f"N = {N}, mu = {mu} on = {int(N*on_over_n)}")
            modularities_base.append(mod_base)
            n_communities_base.append(n_coms_base)
            print(f'\n\n Ended: N - {N} \n\n')


pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, MD_thresholds), open("data/benchmark/b3b", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, MD_thresholds = pickle.load(open("data/benchmark/b3b", 'rb'))
create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, MD_thresholds, "MD thresholds", "b3b")
