import matplotlib.pyplot as plt

"""
Code copied from my another repository
Not all method are useful in this project
"""


def plot_measure_results_data(errors, error=None, title_base='MSE', title_ending=' through epochs', labels=["base model", "momentum model", "RMSProp model"], colors=["green", "blue", "orange", "red", "yellow", "magenta", "black", "brown"], xlabel='epochs', ylabel='MSE', from_error=0, show=True, x=None, save_name=None, log=False, log_y=False):
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
