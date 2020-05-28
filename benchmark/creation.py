from benchmark.methods import create_benchmark

N_list = [500, 1000]
mu_list = [0.2, 0.5]
on_over_n_list = [0.2, 0.5]
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            create_benchmark(N=N, mu=mu, on_over_n=on_over_n, file_appending="b1_" + str(N) + str(mu) + str(on_over_n))

