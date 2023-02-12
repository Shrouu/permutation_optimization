import numpy as np


def f1(x, data):
    D = len(x)
    f1 = 1
    data = data[x, :]
    for j in range(D - 1):
        if data[j][1] != data[j + 1][1]:
            f1 += 1
    return f1 / D


def f2(x, data):
    D = len(x)
    f2 = 1
    data = data[x, :]
    k = 0
    for j in range(D):
        if data[j][3] == "无对比颜色":
            data[j][3] = data[j][2]
    for j in range(D - 1):
        k += 1
        if data[j][3] != data[j][2]:
            f2 += 1
            k = 0
        if data[j][2] != data[j + 1][3]:
            f2 += 1
            k = 0
        elif k == 5:
            f2 += 1
            k = 0
    return f2 / D


def f3(x, data):
    D = len(x)
    data[0] = data[0][0:D,]
    f3 = 0
    data = data[x, :]
    k = 0
    for j in range(D - 1):
        if data[j, 4] == "四驱":
            k += 1
        else:
            if k == 1:
                f3 += 1
            if k >= 4:
                f3 += k - 3
            k = 0
    return f3 / D


def f4(x, data):
    pass
