import numpy as np


def main(x, data):
    D = len(x)
    data[0] = data[0][0:D, ]
    tables = [[data[0][:, 0], data[0][:, 1], data[0][:, 2], data[0][:, 3], data[0][:, 6]]]
    tables = np.array(tables)[0].T
    f2 = 1
    tables = tables[x, :]
    k = 0
    for j in range(D):
        if tables[j][3] == '无对比颜色':
            tables[j][3] = tables[j][2]
    for j in range(D - 1):
        k += 1
        if tables[j][3] != tables[j][2]:
            f2 += 1
            k = 0
        if tables[j][2] != tables[j + 1][3]:
            f2 += 1
            k = 0
        elif k == 5:
            f2 += 1
            k = 0
    return f2 / D
