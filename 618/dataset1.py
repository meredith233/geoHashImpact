import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# x = []
# y = []
dataList = []
# # 总路径
path = "D:\JetBrains\PycharmProjects\geoHashImpact\Gowalla_totalCheckins.txt"
with open(path, 'r+') as fp:
    for line in fp.readlines()[0::100]:
        item_list = line.split('	')
        # x.append(float(item_list[2]))
        # y.append(float(item_list[3]))
        dataList.append([float(item_list[2]), float(item_list[3])])

# # 绘制散点图
# plt.scatter(x, y, 1, c='black')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter Plot')
#
# # 显示图像
# plt.show()
df = pd.DataFrame(dataList, columns=['lat', 'lon'])
st.map(df)
