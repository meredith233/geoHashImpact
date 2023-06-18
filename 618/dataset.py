import os
import matplotlib.pyplot as plt

x = []
y = []
# # 总路径
path = "../Data/{}/Trajectory"
for i in range(182):
    current_path = path.format(str(i).zfill(3))
    plts = os.scandir(current_path)
    for item in plts:
        path_item = current_path + "\\" + item.name
        with open(path_item, 'r+') as fp:
            for line in fp.readlines()[6::600]:
                item_list = line.split(',')
                x.append(float(item_list[0]))
                y.append(float(item_list[1]))

# 绘制散点图
plt.scatter(x, y, 1, c='black')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

# 显示图像
plt.show()
