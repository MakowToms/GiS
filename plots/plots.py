import matplotlib.pyplot as plt

"""
Code copied from my another repository
Not all method are useful in this project
"""


def plot_measure_results_data(errors, error=None, title_base='MSE', title_ending=' through epochs', labels=["base model", "momentum model", "RMSProp model"], colors=["green", "blue", "red", "magenta", "black", "brown", "orange", "yellow",  "red", "magenta"], xlabel='epochs', ylabel='MSE', from_error=0, show=True, x=None, save_name=None, log=False, log_y=False):
    n = len(errors[0])
    if x is None:
        x = [i for i in range(from_error, n)]
    for i in range(len(errors)):
        plt.plot(x, errors[i][from_error:], color=colors[i])
    if error is not None:
        for i in range(len(errors)):
            plt.plot(x, [error[i]] * len(errors[i][from_error:]), color=colors[i], linestyle=':')
    if log:
        plt.xscale('log')
    if log_y:
        plt.yscale('log')
    plt.legend(bbox_to_anchor=(-0.01, 1.07, 1., .107), loc=3, ncol=2, labels=labels)
    plt.title(title_base + title_ending)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if save_name is not None:
        plt.savefig(save_name)
    if show:
        plt.show()


def create_8_plots(times, nmis, modularities, n_communities, modularities_base, n_communities_base, labels, x, xlabel, base_save_name):
    plot_measure_results_data(times[:4], x=x, labels=labels[:4], title_base="Time", title_ending="", ylabel="Time", xlabel=xlabel, save_name="plots/" + base_save_name + "1_time")
    plot_measure_results_data(nmis[:4], x=x, labels=labels[:4], title_base="Mutual information", title_ending="", ylabel="Normalized mutual information", xlabel=xlabel, save_name="plots/" + base_save_name + "1_nmi")
    plot_measure_results_data(modularities[:4], error=modularities_base, x=x, labels=labels[:4], title_base="Modularities", title_ending="", ylabel="Link belong modularity", xlabel=xlabel, save_name="plots/" + base_save_name + "1_modularity")
    plot_measure_results_data(n_communities[:4], error=n_communities_base, x=x, labels=labels[:4], title_base="Communities", title_ending="", ylabel="Number of communities", xlabel=xlabel, save_name="plots/" + base_save_name + "1_ncoms")
    plot_measure_results_data(times[4:], x=x, labels=labels[4:], title_base="Time", title_ending="", ylabel="Time", xlabel=xlabel, save_name="plots/" + base_save_name + "2_time")
    plot_measure_results_data(nmis[4:], x=x, labels=labels[4:], title_base="Mutual information", title_ending="", ylabel="Normalized mutual information", xlabel=xlabel, save_name="plots/" + base_save_name + "2_nmi")
    plot_measure_results_data(modularities[4:], error=modularities_base, x=x, labels=labels[4:], title_base="Modularities", title_ending="", ylabel="Link belong modularity", xlabel=xlabel, save_name="plots/" + base_save_name + "2_modularity")
    plot_measure_results_data(n_communities[4:], error=n_communities_base, x=x, labels=labels[4:], title_base="Communities", title_ending="", ylabel="Number of communities", xlabel=xlabel, save_name="plots/" + base_save_name + "2_ncoms")
