import numpy as np


def main(x, data):
    D = len(x)
    data[0] = data[0][0:D,]
    tables = [
        [data[0][:, 0], data[0][:, 1], data[0][:, 2], data[0][:, 3], data[0][:, 6]]
    ]
    tables = np.array(tables)[0].T
    f3 = 0
    tables = tables[x, :]
    t1 = 0
    t2 = 0
    t3 = 0

    return f3 / D
