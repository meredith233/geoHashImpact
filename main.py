# 数据集的 维度 经度 高度 日期 时间
#
#
import os
import matplotlib.pyplot as plt
import numpy as np

import constants
from geo import encode_geohash, decode_geohash
from utils import cal_dist

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
lat = []  # 维度
lng = []  # 经度
# 总路径
path = "./Data/001/Trajectory"
# 001的路径
# print(os.listdir(os.getcwd()+"\\Geolife Trajectories 1.3"+"\\Data"+"\\003"+"\\Trajectory"
plts_001 = os.scandir(path)
# 每一个文件的绝对路径
for item in plts_001:
    path_item = path + "\\" + item.name
    with open(path_item, 'r+') as fp:
        for item in fp.readlines()[6::600]:
            item_list = item.split(',')
            lat.append(item_list[0])
            lng.append(item_list[1])

lat_new = [float(x) for x in lat]
lng_new = [float(x) for x in lng]

print(lat_new[0], lng_new[0])
lat_hash, lng_hash = encode_geohash(lat_new[0], lng_new[0])
decode_geohash(lat_hash, lng_hash)
# print(x2, y2)
#
# print(cal_dist(lat_new[0], lng_new[0], x2, y2))
