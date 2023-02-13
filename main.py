# -*- coding: utf-8 -*-
from MyProblem import MyProblem  # 导入自定义问题接口
import dataIO as dataIO
import geatpy as ea  # import geatpy

if __name__ == "__main__":
    datapath = "F:\\大学相关\\竞赛\\排产相关赛题\\100组数据集\\数据集\\data_103.csv"
    xcount, data = dataIO.read_data(datapath)
    print("readData: " + datapath)

    # 实例化问题对象
    problem = MyProblem(M=3, data=data)
    # 构建算法
    algorithm = ea.moea_NSGA2_templet(
        problem,
        ea.Population(Encoding="P", NIND=200),
        MAXGEN=200,  # 最大进化代数
        logTras=10,
    )  # 表示每隔多少代记录一次日志信息，0表示不记录。
    # 求解
    res = ea.optimize(
        algorithm,
        verbose=False,
        drawing=1,
        outputMsg=True,
        drawLog=False,
        saveFlag=True,
    )
    print(res)
