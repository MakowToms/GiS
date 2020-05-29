from benchmark.methods import test_ndocd
from plots.plots import plot_measure_results_data, create_8_plots
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
modification_percents = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
modification_numbers = [5, 10, 20, 30, 40, 50]
MD_threshold = 0.3
JS_threshold = 0.3
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            this_times = []
            this_nmis = []
            this_mods = []
            this_ncoms = []
            for modification_percent in modification_percents:
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold, modification=True, modification_percent=modification_percent, modification_number=10, modification_type="percent")
                this_times.append(time)
                this_nmis.append(nmi)
                this_mods.append(mod_ndocd)
                this_ncoms.append(n_coms)
                print(f'Ended: percent - {modification_percent}, N - {N}, time - {time} \n')
            times.append(this_times)
            nmis.append(this_nmis)
            modularities.append(this_mods)
            n_communities.append(this_ncoms)
            labels.append(f"N = {N}, mu = {mu} on = {int(N*on_over_n)}")
            modularities_base.append(mod_base)
            n_communities_base.append(n_coms_base)
            print(f'\n\n Ended: N - {N} \n\n')


# plot_measure_results_data(times[:4], x=modification_percents, labels=labels[:4], title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="JS and MD thresholds", save_name="plots/b1c1_time")
# plot_measure_results_data(nmis[:4], x=modification_percents, labels=labels[:4], title_base="Mutual information for different number of vertices", title_ending="", ylabel="Normalized mutual information", xlabel="JS and MD thresholds", save_name="plots/b1c1_nmi")
# plot_measure_results_data(modularities[:4], error=modularities_base, x=modification_percents, labels=labels[:4], title_base="Modularities for different number of vertices", title_ending="", ylabel="Link belong modularity", xlabel="JS and MD thresholds", save_name="plots/b1c1_modularity")
# plot_measure_results_data(n_communities[:4], error=n_communities_base, x=modification_percents, labels=labels[:4], title_base="Communities for different number of vertices", title_ending="", ylabel="Number of communities", xlabel="JS and MD thresholds", save_name="plots/b1c1_ncoms")
# plot_measure_results_data(times[4:], x=modification_percents, labels=labels[4:], title_base="Time for different number of vertices", title_ending="", ylabel="Time", xlabel="JS and MD thresholds", save_name="plots/b1c2_time")
# plot_measure_results_data(nmis[4:], x=modification_percents, labels=labels[4:], title_base="Mutual information for different number of vertices", title_ending="", ylabel="Normalized mutual information", xlabel="JS and MD thresholds", save_name="plots/b1c2_nmi")
# plot_measure_results_data(modularities[4:], error=modularities_base, x=modification_percents, labels=labels[4:], title_base="Modularities for different number of vertices", title_ending="", ylabel="Link belong modularity", xlabel="JS and MD thresholds", save_name="plots/b1c2_modularity")
# plot_measure_results_data(n_communities[4:], error=n_communities_base, x=modification_percents, labels=labels[4:], title_base="Communities for different number of vertices", title_ending="", ylabel="Number of communities", xlabel="JS and MD thresholds", save_name="plots/b1c2_ncoms")
pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, modification_percents), open("data/benchmark/b1c", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, modification_percents = pickle.load(open("data/benchmark/b1c", 'rb'))
create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, modification_percents, "percent of left edges", "b1c")


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
            this_times = []
            this_nmis = []
            this_mods = []
            this_ncoms = []
            for modification_number in modification_numbers:
                time, nmi, mod_ndocd, mod_base, n_coms, n_coms_base = test_ndocd(folder, file_appending="b1_" + str(N) + str(mu) + str(on_over_n), MD_threshold=MD_threshold, JS_threshold=JS_threshold, modification=True, modification_number=modification_number, modification_type="number")
                this_times.append(time)
                this_nmis.append(nmi)
                this_mods.append(mod_ndocd)
                this_ncoms.append(n_coms)
                print(f'Ended: number - {modification_number}, N - {N}, time - {time} \n')
            times.append(this_times)
            nmis.append(this_nmis)
            modularities.append(this_mods)
            n_communities.append(this_ncoms)
            labels.append(f"N = {N}, mu = {mu} on = {int(N*on_over_n)}")
            modularities_base.append(mod_base)
            n_communities_base.append(n_coms_base)
            print(f'\n\n Ended: N - {N} \n\n')


pickle.dump((times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, modification_numbers), open("data/benchmark/b1d", 'wb'))
# times, nmis, modularities, n_communities, labels, modularities_base, n_communities_base, modification_numbers = pickle.load(open("data/benchmark/b1d", 'rb'))
create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, modification_numbers, "minimal number of t_ij to left edge", "b1d")

