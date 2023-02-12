import numpy as np


def main(x, data):
    D = len(x)
    data[0] = data[0][0:D, ]
    tables = [[data[0][:, 0], data[0][:, 1], data[0][:, 2], data[0][:, 3], data[0][:, 6]]]
    tables = np.array(tables)[0].T
    f3 = 0
    tables = tables[x, :]
    k = 0
    for j in range(D - 1):
        if tables[j, 4] == '四驱':
            k += 1
        else:
            if k == 1:
                f3 += 1
            if k >= 4:
                f3 += (k - 3)
            k = 0
    return f3 / D
