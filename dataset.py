import os
from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

objects = []
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
                objects.append([float(item_list[1]), float(item_list[0])])


