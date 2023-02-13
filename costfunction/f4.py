import numpy as np

# 目标四：经过三道工序时间尽可能短
def main(x, data):
    D = len(x)
    data[0] = data[0][0:D,]
    tables = [
        [data[0][:, 0], data[0][:, 1], data[0][:, 2], data[0][:, 3], data[0][:, 6]]
    ]
    tables = np.array(tables)[0].T
    f4 = 0
    tables = tables[x, :]
    # 各车间的时间（以秒为单位）
    t1 = 0
    t2 = 0
    t3 = 0
    ## 考虑焊装车间完工时间
    ct = 0  # 当前设备已使用时间
    for j in range(D - 1):
        # 先加上当前车焊装的时间
        ct += 80
        t1 += 80
        # 如果接下来需要换设备，需要满足时间条件
        if tables[j][1] != tables[j + 1][1]:
            # 若工时尚未达到半小时，需要等待切换;已经工作半小时以上，无需等待切换
            if ct <= 2400:
                t1 += 2400 - ct
            ct = 0
        # 如果到最后一个（D-2）了，就把 D-1的时间也加进来
        if (j == D - 2):
            t1 += 80
    ## 考虑涂装车间完工时间
    k = 0
    for j in range(D):
        if tables[j][3] == '无对比颜色':
            tables[j][3] = tables[j][2]
    for j in range(D - 1):
        k += 1
        # 加当前车的涂色时间
        t2 += 40
        # 若当前车车顶车身不同色，需要清洗
        if tables[j][3] != tables[j][2]:
            t2 += 80
            k = 0
        # 如果是最后一个，不再考虑其后的清洗,需要加上D-1的时间
        if(j == D - 2):
            t2 += 40
            break
        # 如果达到连续五次，不管下一个是啥，都要清洗
        if k == 5:
            t2 += 80
            k = 0
            continue  # 这是为了避免重复计算时间
        # 若当前车车身和下一辆车的车顶颜色不同，需要清洗
        if tables[j][2] != tables[j + 1][3]:
            t2 += 80
            k = 0
    ## 考虑总装车间完工时间
    t3 += D * 80
    # 加和
    f4 = t1 + t2 + t3
    return f4 / D
