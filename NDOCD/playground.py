from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix, dok_matrix
import numpy as np


rows    = np.array([0, 1, 1, 2, 3, 3])
columns = np.array([3, 2, 3, 1, 0, 1])
res = np.stack([rows, columns])
res.reshape((1, -1), order='F')
res[0, 4:0:-1]

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
row[1].indices

mask = (j != 0).transpose()
print(mask)

A = np.array([1, 0.1, 0.2, 0.4, 0.7, 0])
B = np.array([0, 0.1, 0, 0.4, 0, 0.1])
(B!=0) * A

A[2] = (row[0] @ (mask)).data

np.argmax(B)

n = 10
a = dok_matrix((1, n))
a[0, 2] = 1
a[0, 7] = 3
a

A[:4] * mask.transpose()

dok_graph = dok_matrix(graph)
dok_graph.toarray()
for i in dok_graph[1].nonzero()[1]:
    print(i)

indices = dok_graph[1].nonzero()[1]
all_ind = np.array([0, 3, 2, 4, 5])

np.all(np.isin(indices, all_ind))

dok_graph[1, :] = dok_graph[2]
dok_graph[:, 1] = dok_graph[2].transpose()

np.sum(dok_graph[1])

row[row[1].indices].toarray()

row[1, 2] = 2
row[1, 2] = 0
row[1].nonzero()
row[1].toarray()
row[1]

row.eliminate_zeros()
row.prune()
row

row.toarray()
np.sum(row, axis=1)

MD_threshold=0.5
JS_threshold=0.5

JS = np.array([0, 1, 1, 0, 0])
MD = np.array([0, 1, 0, 1, 0])
a = np.logical_or(JS > JS_threshold, MD > MD_threshold)
JS[a]

while True:
    vertices_to_add = np.array([])
    print(1)
    if vertices_to_add.shape[0] == 0:
        break

