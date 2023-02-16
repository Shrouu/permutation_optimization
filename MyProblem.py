# -*- coding: utf-8 -*-

import numpy as np
import costF as cost
import geatpy as ea


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self, M=4, data=[], Dim=0):
        name = "MyProblem"  # 初始化name（函数名称，可以随意设置）
        maxormins = [1, 1, 1, 1]  # 初始化maxormins（目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标）
        Dim = Dim  # 初始化Dim（决策变量维数）
        varTypes = [1] * Dim  # 初始化varTypes（决策变量的类型，元素为0表示对应的变量是连续的；1表示是离散的）
        lb = [0] * Dim  # 决策变量下界
        ub = [Dim] * Dim  # 决策变量上界
        lbin = [1] * Dim  # 决策变量下边界（0表示不包含该变量的下边界，1表示包含）
        ubin = [0] * Dim  # 决策变量上边界（0表示不包含该变量的上边界，1表示包含）
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb, ub, lbin, ubin)
        self.data = data

    def evalVars(self, Vars):  # 目标函数
        x = Vars.astype(int)  # 得到决策变量矩阵
        ObjV = cost.costCompute(x, self.data)
        # 采用可行性法则处理约束
        CV = None
        # ObjV = np.hstack([f1, f2, f3, f4])
        return ObjV, CV
