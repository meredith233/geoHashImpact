import os
import folium
from folium.plugins import HeatMap

objects = []
# # 总路径
path = "./Gowalla_totalCheckins.txt"
with open(path, 'r+') as fp:
    for line in fp.readlines()[0::100]:
        item_list = line.split('	')
        objects.append([float(item_list[2]), float(item_list[3])])

san_map = folium.Map(location=[30.2691029532, -97.7493953705], zoom_start=12, width='100%', height='100%')
HeatMap(objects).add_to(san_map)

file_path = r"./AirQualityMap.html"

# 保存为html文件
san_map.save(file_path)
