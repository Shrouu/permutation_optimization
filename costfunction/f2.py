import numpy as np

# 目标二：涂装车间喷漆切换次数尽可能小（有改动）
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
        # 若当前车车顶车身不同色，需要清洗
        if tables[j][3] != tables[j][2]:
            f2 += 1
            k = 0
        # 如果是最后一个，不再考虑其后的清洗
        if(j == D - 2):
            break
        # 如果达到连续五次，不管下一个是啥，都要清洗
        if k == 5:
            f2 += 1
            k = 0
            continue  # 这是为了避免重复计算时间
        # 若当前车车身和下一辆车的车顶颜色不同，需要清洗
        if tables[j][2] != tables[j + 1][3]:
            f2 += 1
            k = 0
    return f2 / D
