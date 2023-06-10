# 数据集的 维度 经度 高度 日期 时间
#
#
import math
import os
import random

import matplotlib.pyplot as plt
import numpy as np

import constants
import laplace
import utils
from geo import encode_geohash, decode_geohash

from statistics import mean

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
lat = []  # 维度
lng = []  # 经度
# 总路径
path = "./Data/{}/Trajectory"
for i in range(182):
    current_path = path.format(str(i).zfill(3))
    plts = os.scandir(current_path)
    for item in plts:
        path_item = current_path + "\\" + item.name
        with open(path_item, 'r+') as fp:
            for line in fp.readlines()[6::600]:
                item_list = line.split(',')
                lat.append(item_list[0])
                lng.append(item_list[1])
                break
        break

lat_new = [float(x) for x in lat]
lng_new = [float(x) for x in lng]

# 随机取一个基准点
baseLoc = random.randint(0, 181)
baseX = lat_new[baseLoc]
baseY = lng_new[baseLoc]

lat_hash, lng_hash = encode_geohash(baseX, baseY)


def do_r():
    dis_single = []
    for _ in range(1000):
        laplace.process(baseX, baseY)
        lat_hash_arr = [c for c in lat_hash]
        lng_hash_arr = [c for c in lng_hash]
        # 后5位随机取一位扰动
        a = constants.geo_num - 1
        lat_hash_arr[a] = utils.change_item(lat_hash_arr[a])
        lng_hash_arr[a] = utils.change_item(lng_hash_arr[a])
        lat_hash_fin = "".join(lat_hash_arr)
        lng_hash_fin = "".join(lng_hash_arr)
        # 扰动结束

        # 获取最终坐标
        target_lat, target_lng = decode_geohash(lat_hash_fin, lng_hash_fin)
        dis_single.append(utils.distance(target_lat, target_lng, baseX, baseY))
    print(mean(dis_single))
    laplace.next_step()
    return mean(dis_single)


dis_single_fin = []
dis_lap = []
e_list = [round(i, 1) for i in np.arange(0.1, 1.1, 0.1)]
for ep in e_list:
    constants.epsilon = ep
    constants.e_epsilon = math.exp(constants.epsilon)
    constants.rate_of_1_to_1 = constants.e_epsilon / (constants.e_epsilon + 1)
    constants.rate_of_0_to_1 = 1 / (constants.e_epsilon + 1)
    dis_single_fin.append(do_r())

plt.ylim(min(dis_single_fin) - 10, max(dis_single_fin) + 30)
plt.xlim(0, 1)

plt.title("关系图")
plt.xlabel("epsilon")  # 定义x坐标轴名称
plt.ylabel("distance")  # 定义y坐标轴名称
plt.plot(e_list, dis_single_fin)  # 绘图
plt.plot(e_list, laplace.get_dis())
plt.show()  # 展示
