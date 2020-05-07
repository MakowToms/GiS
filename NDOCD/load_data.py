import numpy as np
from scipy.sparse import coo_matrix
import pandas as pd


def random_graph(size=100, edges=1000):
    cols = np.random.randint(0, size, size=(edges))
    rows = np.random.randint(0, size, size=(edges))
    return create_graph_by_cols_and_rows(size, cols, rows)


def create_graph_by_cols_and_rows(size, cols, rows):
    vals = np.ones(shape=[cols.shape[0]])
    rang = np.arange(size)
    mat = coo_matrix((vals, (rows, cols)), shape=[size, size]).todok()
    mat[cols, rows] = vals
    mat[rang, rang] = np.zeros(shape=[size])
    mat = mat.tocsr()
    mat.data = np.ones(mat.data.shape[0])
    return mat


def get_actors_graph():
    data = pd.read_csv("data/allActorsRelation.csv", delimiter=";")
    uniques = np.unique(data.iloc[:, 0:2])
    size = uniques.shape[0]
    to_replace = dict((val, i) for (i, val) in enumerate(uniques))
    cols = np.array(data.iloc[:, 0].replace(to_replace))
    rows = np.array(data.iloc[:, 1].replace(to_replace))
    return create_graph_by_cols_and_rows(size, cols, rows)


def get_amazon_graph():
    data = pd.read_csv("data/amazon/com-amazon.ungraph.txt", delimiter="\t", comment='#')
    uniques = np.unique(data.iloc[:, 0:2])
    size = uniques.shape[0]
    to_replace = dict((val, i) for (i, val) in enumerate(uniques))
    cols = replace(np.array(data.iloc[:, 0]), to_replace)
    rows = replace(np.array(data.iloc[:, 1]), to_replace)
    return create_graph_by_cols_and_rows(size, cols, rows)


def get_email_graph():
    data = pd.read_csv("data/email/email-Eu-core.txt", delimiter=" ", comment='#', header=None)
    uniques = np.unique(data.iloc[:, 0:2])
    size = uniques.shape[0]
    to_replace = dict((val, i) for (i, val) in enumerate(uniques))
    cols = replace(np.array(data.iloc[:, 0]), to_replace)
    rows = replace(np.array(data.iloc[:, 1]), to_replace)
    return create_graph_by_cols_and_rows(size, cols, rows)


def rewrite_email_communities():
    data = pd.read_csv("data/email/email-Eu-core-department-labels.txt", delimiter=" ", comment='#', header=None)
    with open("data/email/email-communities", 'w') as f:
        for i in range(data.iloc[:, 1].max()):
            community = list(data[data.iloc[:, 1] == i+1].iloc[:, 0])
            to_write = ""
            for index in community:
                to_write += str(index) + " "
            to_write = to_write[:-1]
            f.write(to_write + "\n")


def replace(array, to_replace):
    new_array = np.zeros(array.shape)
    for key in to_replace:
        new_array[array == key] = to_replace[key]
    return new_array


def write_communities_to_file(communities, file_name):
    with open(file_name, 'w') as f:
        for community in communities:
            to_write = ""
            for index in community.indices:
                to_write += str(index) + " "
            to_write = to_write[:-1]
            f.write(to_write + "\n")
