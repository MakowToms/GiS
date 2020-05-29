from benchmark.methods import create_benchmark, create_benchmark_weighted

N_list = [500, 1000]
mu_list = [0.2, 0.5]
on_over_n_list = [0.2, 0.5]
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            create_benchmark(N=N, mu=mu, on_over_n=on_over_n, file_appending="b1_" + str(N) + str(mu) + str(on_over_n))


N_list = [500, 1000]
on_over_n_list = [0.2, 0.5]
for N in N_list:
    for on_over_n in on_over_n_list:
        create_benchmark_weighted(N=N, on_over_n=on_over_n, file_appending="b1_" + str(N) + str(on_over_n))


N_list = [i*200 for i in range(1, 11)]
for N in N_list:
    create_benchmark(N=N, file_appending="b2_" + str(N))

N_list = [500, 1000]
mu_list = [0.1, 0.2]
on_over_n_list = [0.1, 0.2]
for N in N_list:
    for mu in mu_list:
        for on_over_n in on_over_n_list:
            create_benchmark(N=N, mu=mu, on_over_n=on_over_n, file_appending="b3_" + str(N) + str(mu) + str(on_over_n))
