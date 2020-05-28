from benchmark.methods import test_ndocd
from plots.plots import plot_measure_results_data
import pickle

folder = "data/benchmark/"
N_list = [500, 1000]
mu_list = [0.2, 0.5]
on_over_n_list = [0.2, 0.5]
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
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
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


plot_measure_results_data(times, x=JS_thresholds, labels=labels, title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="JS and MD thresholds", save_name="plots/b1z_time")
plot_measure_results_data(nmis, x=JS_thresholds, labels=labels, title_base="Mutual information for different number of vertices", title_ending="", ylabel="Normalized mutual information", xlabel="JS and MD thresholds", save_name="plots/b1z_nmi")
plot_measure_results_data(modularities, x=JS_thresholds, labels=labels, title_base="Modularities for different number of vertices", title_ending="", ylabel="Link belong modularity", xlabel="JS and MD thresholds", save_name="plots/b1z_modularity")
plot_measure_results_data(n_communities, x=JS_thresholds, labels=labels, title_base="Communities for different number of vertices", title_ending="", ylabel="Number of communities", xlabel="JS and MD thresholds", save_name="plots/b1z_ncoms")
modularities_base
n_communities_base
pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds), open("data/benchmark/b1z", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds = pickle.load(open("data/benchmark/b1z", 'rb'))


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
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
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


plot_measure_results_data(times, x=JS_thresholds, labels=labels, title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="JS threshold", save_name="plots/b1a_time")
plot_measure_results_data(nmis, x=JS_thresholds, labels=labels, title_base="Mutual information for different number of vertices", title_ending="", ylabel="Normalized mutual information", xlabel="JS threshold", save_name="plots/b1a_nmi")
plot_measure_results_data(modularities, x=JS_thresholds, labels=labels, title_base="Modularities for different number of vertices", title_ending="", ylabel="Link belong modularity", xlabel="JS threshold", save_name="plots/b1a_modularity")
plot_measure_results_data(n_communities, x=JS_thresholds, labels=labels, title_base="Communities for different number of vertices", title_ending="", ylabel="Number of communities", xlabel="JS threshold", save_name="plots/b1a_ncoms")
modularities_base
n_communities_base
pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds), open("data/benchmark/b1a", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds = pickle.load(open("data/benchmark/b1a", 'rb'))

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
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold)
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


plot_measure_results_data(times, x=MD_thresholds, labels=labels, title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="MD threshold", save_name="plots/b1b_time")
plot_measure_results_data(nmis, x=MD_thresholds, labels=labels, title_base="Mutual information for different number of vertices", title_ending="", ylabel="Normalized mutual information", xlabel="MD threshold", save_name="plots/b1b_nmi")
plot_measure_results_data(modularities, x=MD_thresholds, labels=labels, title_base="Modularities for different number of vertices", title_ending="", ylabel="Link belong modularity", xlabel="MD threshold", save_name="plots/b1b_modularity")
plot_measure_results_data(n_communities, x=MD_thresholds, labels=labels, title_base="Communities for different number of vertices", title_ending="", ylabel="Number of communities", xlabel="MD threshold", save_name="plots/b1b_ncoms")
modularities_base
n_communities_base
pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, MD_thresholds), open("data/benchmark/b1b", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, JS_thresholds = pickle.load(open("data/benchmark/b1b", 'rb'))
