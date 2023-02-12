"""
Main part of program, optimization the standard data in certain path.
"""


import dataIO as dataIO
from Genetic import *


def main():
    datapath = "F:\\大学相关\\竞赛\\排产相关赛题\\100组数据集\\数据集"
    filelist = dataIO.read_filename(datapath)
    for file in filelist:
        xcount, data = dataIO.read_data(datapath + "\\" + file)
        print("readData: " + file)
        GenA = genetic(xcount, data)
        GenA.popInit()
        GenA.popDominatSort()


if __name__ == "__main__":
    main()
