import os
import folium
from folium.plugins import HeatMap

objects = []
# # 总路径
path = "./Data/{}/Trajectory"
for i in range(10):
    current_path = path.format(str(i).zfill(3))
    plts = os.scandir(current_path)
    for item in plts:
        path_item = current_path + "\\" + item.name
        with open(path_item, 'r+') as fp:
            for line in fp.readlines()[6::600]:
                item_list = line.split(',')
                objects.append([float(item_list[0]), float(item_list[1])])

san_map = folium.Map(location=[39.90830689265166, 116.39762575401475], zoom_start=12, width='100%', height='100%', tiles='Stamen Toner')
HeatMap(objects, gradient={
    0.0: 'black',
    0.3: 'black',
    0.5: 'grey',
    0.7: 'white',
    1.0: 'white'
}).add_to(san_map)

file_path = r"./AirQualityMap.html"

# 保存为html文件
san_map.save(file_path)
