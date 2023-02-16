import numpy as np
import pandas as pd
import os


def read_filename(path):
    return os.listdir(path)


def read_data(filename):
    xcount = filename.split("_")[1].split(".")[0]
    xcount = int(xcount)
    data = pd.read_csv(filename).values.tolist()
    data = np.array(data)
    data = data[0:xcount,]
    tables = [[data[:, 0], data[:, 1], data[:, 2], data[:, 3], data[:, 6]]]
    tables = np.array(tables)[0].T
    return xcount, tables


if __name__ == "__main__":
    datapath = "F:\\大学相关\\竞赛\\排产相关赛题\\处理后数据"
    filelist = read_filename(datapath)
    for filename in filelist:
        data = pd.read_csv(datapath + "//" + filename)
        print(filename + ": " + str(len(data)))
