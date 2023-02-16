import numpy as np


def costCompute(x, data):
    populationSize = len(x)
    Datalenth = len(x[0])
    fFounditions = [1, 1, 1, 1]
    MatrixF1 = []
    MatrixF2 = []
    MatrixF3 = []
    MatrixF4 = []
    for individual in x:  # 对于population中的每个个体单独计算objective fuction
        tables = data[individual, :]  # 按照个体对数据排序

        # 计算f1,t1
        f1 = 1
        t1 = 0
        ct = 0  # 当前设备已使用时间
        for j in range(Datalenth - 1):
            # 单辆车焊接时间
            ct += 80
            t1 += 80
            if tables[j][1] != tables[j + 1][1]:
                f1 += 1
                if ct <= 1800:  # 是否连续焊接达到半小时
                    t1 += 1800 - ct
                    ct = 0
        t1 += 80
        MatrixF1.append(f1 / Datalenth / fFounditions[0])

        # 计算f2,t2
        f2 = 1
        k = 0
        t2 = 0
        for j in range(Datalenth):
            if tables[j][3] == "无对比颜色":
                tables[j][3] = tables[j][2]
        for j in range(Datalenth - 1):
            k += 1
            # 单车喷涂时间
            t2 += 40
            # 若当前车车顶车身不同色，需要清洗
            if tables[j][3] != tables[j][2]:
                t2 += 80
                f2 += 1
                k = 0
            # 如果达到连续五次，不管下一个是啥，都要清洗
            if k == 5:
                t2 += 80
                f2 += 1
                k = 0
                continue  # 这是为了避免重复计算时间
            # 若当前车车身和下一辆车的车顶颜色不同，需要清洗
            if tables[j][2] != tables[j + 1][3]:
                t2 += 80
                f2 += 1
                k = 0
        # 单独考虑最后一辆车是否还需要因为车顶车身颜色不同再清洗一次
        if tables[Datalenth - 1][3] != tables[Datalenth - 1][2]:
            t2 += 80 + 40
            f2 += 1
        else:
            t2 += 40
        MatrixF2.append(f2 / Datalenth / fFounditions[1])

        # 计算f3,t3
        f3 = 1
        k = 0
        for j in range(Datalenth - 1):
            if tables[j, 4] == "四驱":
                k += 1
            else:
                if k == 1:
                    f3 += 1
                if k >= 4:
                    f3 += k - 3
                k = 0
        t3 = Datalenth * 80
        MatrixF3.append(f3 / Datalenth / fFounditions[2])
        f4 = t1 + t2 + t3
        MatrixF4.append(f4 / Datalenth / fFounditions[3])
    MatrixF1 = np.array(MatrixF1).reshape([populationSize, 1])
    MatrixF2 = np.array(MatrixF2).reshape([populationSize, 1])
    MatrixF3 = np.array(MatrixF3).reshape([populationSize, 1])
    MatrixF4 = np.array(MatrixF4).reshape([populationSize, 1])
    return np.hstack([MatrixF1, MatrixF2, MatrixF3, MatrixF4])
