import numpy as np
from matplotlib import pyplot as plt

e_list = [round(i, 1) for i in np.arange(0.1, 1.1, 0.1)]

tree = [57.74201644528048, 57.278534480996385, 55.994753190222, 53.7692824780642, 52.60297796422273, 49.15262783127156,
        45.80808555837156, 45.48527789420324, 45.1699456728826, 45.2629630819101]
ours = [46.60417725865591, 44.56792903117255, 44.02939149594654, 43.38692000979885, 42.82662823358409,
        42.06345324978446, 41.29648587554411, 41.20624316358868, 40.15577557815865, 39.54963984633587]
dplip = [66.5977986491467, 57.73474317479995, 52.49321747474079, 52.55810893968891, 51.30751757020297,
         50.46957156674375, 49.918249718222924, 49.78478642121586, 50.897805029291796, 49.9117895440087]
dplpa = [49.11393868158055, 48.28821958218574, 46.38201040963521, 44.28338133473648, 42.22772870570499,
         42.88296541898381, 42.31550049957643, 43.334971061770844, 43.17058913390494, 42.23662165281649]

plt.ylim(30, 90)
plt.xlim(0, 1.1)

plt.title("graph")
plt.xlabel("epsilon")  # 定义x坐标轴名称
plt.ylabel("avg distance")  # 定义y坐标轴名称
plt.plot(e_list, ours, '-D', label="OURS", color='k')  # 绘图
plt.plot(e_list, dplip, '-o', label="DPLIP", color='k')  # 绘图
plt.plot(e_list, dplpa, '-x', label="DPLPA", color='k')  # 绘图
plt.plot(e_list, tree, '-*', label="TREE", color='k')  # 绘图
plt.legend()
plt.show()  # 展示