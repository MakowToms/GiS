from benchmark.methods import create_benchmark

N_list = [100, 500, 1000]
for N in N_list:
    create_benchmark(N, file_appending="b1_" + str(N))

