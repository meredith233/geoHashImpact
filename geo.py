import numpy as np
from matplotlib import pyplot as plt

import constants
from constants import epsilon
from utils import cal_dist


def encode_geohash(latitude, longitude, precision=10):
    """
    将给定的经纬度转化为geohash编码
    """
    lon_hash = ""
    lat_hash = ""
    # 经度范围
    lon_range = (-180.0, 180.0)
    # 纬度范围
    lat_range = (-90.0, 90.0)

    while len(lon_hash) < precision:
        # 二分法判断经纬度所属区间
        mid = (lon_range[0] + lon_range[1]) / 2
        if longitude > mid:
            lon_hash += "1"
            lon_range = (mid, lon_range[1])
        else:
            lon_hash += "0"
            lon_range = (lon_range[0], mid)

        mid = (lat_range[0] + lat_range[1]) / 2
        if latitude > mid:
            lat_hash += "1"
            lat_range = (mid, lat_range[1])
        else:
            lat_hash += "0"
            lat_range = (lat_range[0], mid)

    return lat_hash, lon_hash


def decode_geohash(lat_hash, lon_hash):
    """
    将给定的geohash编码转化为经纬度
    """
    # 经度范围
    lon_range = (-180.0, 180.0)
    # 纬度范围
    lat_range = (-90.0, 90.0)

    for i in range(len(lon_hash)):
        mid = (lon_range[0] + lon_range[1]) / 2
        if lon_hash[i] == "1":
            lon_range = (mid, lon_range[1])
        else:
            lon_range = (lon_range[0], mid)

        mid = (lat_range[0] + lat_range[1]) / 2
        if lat_hash[i] == "1":
            lat_range = (mid, lat_range[1])
        else:
            lat_range = (lat_range[0], mid)

    x1 = lat_range[0]
    y1 = lon_range[0]
    x2 = lat_range[1]
    y2 = lon_range[1]
    S = abs(x2 - x1) * abs(y2 - y1)
    ss = S / 100

    points_x = np.random.uniform(x1, x2, 100)
    points_y = np.random.uniform(y1, y2, 100)

    ep(points_x, points_y, ss)

def ep(points_x, points_y, ss):
    xl = []
    yl = []
    x1 = 39.984094
    y1 = 116.319236

    for i in np.arange(0.1, 1.1, 0.1):
        constants.epsilon = i
        # 对每个点添加拉普拉斯噪声
        noisy_points_x = add_laplace_noise(points_x, ss)
        noisy_points_y = add_laplace_noise(points_y, ss)
        # 随机选择一个带有噪声的点作为生成点

        idx = np.random.randint(100)
        x2, y2 = noisy_points_x[idx], noisy_points_y[idx]
        dist = cal_dist(x1, y1, x2, y2)
        xl.append(i)
        yl.append(dist)
    plt.ylim((min(yl), max(yl)))
    plt.xlim((min(xl), max(xl)))

    plt.title("关系图")
    plt.xlabel("epsilon")  # 定义x坐标轴名称
    plt.ylabel("distance")  # 定义y坐标轴名称
    plt.plot(xl, yl)  # 绘图
    plt.show()  # 展示

def add_laplace_noise(data, sensitivity):
    """
    对每个数据项添加拉普拉斯噪声
    """
    # 计算拉普拉斯分布的比例因子
    scale = sensitivity / epsilon
    # 生成每个数据项的噪声并加上
    noise = np.random.laplace(0, scale, len(data))
    return data + noise
