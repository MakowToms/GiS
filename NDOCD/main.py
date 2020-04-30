from scipy.sparse import csr_matrix, csc_matrix, coo_matrix
import numpy as np


rows    = np.array([0, 1, 1, 2, 3, 3])
columns = np.array([3, 2, 3, 1, 0, 1])
values = np.ones([columns.shape[0]])
graph = coo_matrix((values, (rows, columns)), shape=(4, 4))
print(graph)
graph

csr_matrix(([0], ([0], [0])), shape=(3, 3))

cols = csc_matrix(graph)
print(cols)
row = csr_matrix(graph)
print(row)

for i in cols:
    print(i)
for j in row[1]:
    print(j[0])
    print(j)
j.data
j.indices
row.data
row.indices

mask = (j != 0).transpose()
print(mask)

A[2] = (row[0] @ (mask)).data


A = np.array([1, 0.1, 0.2, 0.4, 0.7, 0])
B = np.array([0, 0.1, 0, 0.4, 0, 0.1])
(B!=0) * A