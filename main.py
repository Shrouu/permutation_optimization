# -*- coding: utf-8 -*-
from MyProblem import MyProblem  # 导入自定义问题接口
import dataIO as dataIO
import geatpy as ea  # import geatpy

if __name__ == "__main__":
    datapath = "F:\\大学相关\\竞赛\\排产相关赛题\\数据集"
    filelist = dataIO.read_filename(datapath)

    totalHV = 0
    count = 0
    for file in filelist:
        xcount, data = dataIO.read_data(datapath + "\\" + file)
        print("readData: " + file)
        # xcount, data = dataIO.read_data(datapath + "\\data_1021.csv")

        # 实例化问题对象
        problem = MyProblem(data=data, Dim=xcount)
        # 构建算法
        algorithm = ea.moea_NSGA2_templet(
            problem,
            ea.Population(Encoding="P", NIND=60),
            MAXGEN=600,  # 最大进化代数
            logTras=10,
            data=data,
        )  # 表示每隔多少代记录一次日志信息，0表示不记录。
        # 求解
        res = ea.optimize(
            algorithm,
            verbose=False,
            drawing=0,
            outputMsg=True,
            drawLog=False,
            saveFlag=True,
            xcount=xcount,
        )
        count += 1
        totalHV += float(res["hv"])
        # break
    print("Main HV of this time optimization is: " + str(totalHV / count))
