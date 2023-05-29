import random
import math
import numpy as np

import constants


def distance(lat1, lon1, lat2, lon2):
    # 地球半径，单位：米
    r = 6371000

    # 将经纬度转换为弧度
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # 计算距离
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = r * c

    return d


def cal_dist(x1, y1, x2, y2):
    # 定义两个二维向量（点）
    point1 = np.array([x1, y1])
    point2 = np.array([x2, y2])

    # 计算两点之间的欧几里得距离
    return np.linalg.norm(point1 - point2, axis=0)


def change_item(item):
    if item == '1':
        return change_1()
    else:
        return change_0()


def change_1():
    if positive_rate(constants.rate_of_1_to_1):
        return '1'
    else:
        return '0'


def change_0():
    if positive_rate(constants.rate_of_0_to_1):
        return '1'
    else:
        return '0'


def positive_rate(x):
    random_val = random.random()
    return random_val < x
