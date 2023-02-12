import numpy as np


def main(x, data):
    D = len(x)
    data[0] = data[0][0:D,]
    tables = [
        [data[0][:, 0], data[0][:, 1], data[0][:, 2], data[0][:, 3], data[0][:, 6]]
    ]
    tables = np.array(tables)[0].T
    f1 = 1
    tables = tables[x, :]
    for j in range(D - 1):
        if tables[j][1] != tables[j + 1][1]:
            f1 += 1
    return f1 / D
