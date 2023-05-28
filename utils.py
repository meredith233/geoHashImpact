import numpy as np


def cal_dist(x1, y1, x2, y2):
    # 定义两个二维向量（点）
    point1 = np.array([x1, y1])
    point2 = np.array([x2, y2])

    # 计算两点之间的欧几里得距离
    return np.linalg.norm(point1 - point2, axis=0)
