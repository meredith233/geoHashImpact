import os
from collections import deque

from matplotlib import pyplot as plt, patches

curve = []

stack = deque()


def get_left_bottom(x1, x2, y1, y2):
    return x1, (x1 + x2) / 2, y1, (y1 + y2) / 2


def get_left_top(x1, x2, y1, y2):
    return x1, (x1 + x2) / 2, (y1 + y2) / 2, y2


def get_right_bottom(x1, x2, y1, y2):
    return (x1 + x2) / 2, x2, y1, (y1 + y2) / 2


def get_right_top(x1, x2, y1, y2):
    return (x1 + x2) / 2, x2, (y1 + y2) / 2, y2


def filter_point(x1, x2, y1, y2, points):
    res = []
    for p in points:
        if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
            res.append(p)
    return res


# 定义维度 0-180 经度 0-360
# 希尔伯特一阶从左下到左上到右上到右下， 编排为 0 -- 3
# direction 0向上 1向右 2向下 3向左
def hil(x1, x2, y1, y2, points, direction):
    if direction == 0:
        hil0(x1, x2, y1, y2, points)
    elif direction == 1:
        hil1(x1, x2, y1, y2, points)
    elif direction == 2:
        hil2(x1, x2, y1, y2, points)
    else:
        hil3(x1, x2, y1, y2, points)


# 朝上
def hil0(x11, x22, y11, y22, points):
    record = []
    analyze(x11, x22, y11, y22, points, 1, get_left_bottom, record)
    analyze(x11, x22, y11, y22, points, 0, get_left_top, record)
    analyze(x11, x22, y11, y22, points, 0, get_right_top, record)
    analyze(x11, x22, y11, y22, points, 3, get_right_bottom, record)


# 朝右
def hil1(x11, x22, y11, y22, points):
    record = []
    analyze(x11, x22, y11, y22, points, 0, get_left_bottom, record)
    analyze(x11, x22, y11, y22, points, 1, get_right_bottom, record)
    analyze(x11, x22, y11, y22, points, 1, get_right_top, record)
    analyze(x11, x22, y11, y22, points, 2, get_left_top, record)


# 朝下
def hil2(x11, x22, y11, y22, points):
    record = []
    analyze(x11, x22, y11, y22, points, 3, get_right_top, record)
    analyze(x11, x22, y11, y22, points, 2, get_right_bottom, record)
    analyze(x11, x22, y11, y22, points, 2, get_left_bottom, record)
    analyze(x11, x22, y11, y22, points, 1, get_left_top, record)


# 朝左
def hil3(x11, x22, y11, y22, points):
    record = []
    analyze(x11, x22, y11, y22, points, 2, get_right_top, record)
    analyze(x11, x22, y11, y22, points, 3, get_left_top, record)
    analyze(x11, x22, y11, y22, points, 3, get_left_bottom, record)
    analyze(x11, x22, y11, y22, points, 0, get_right_bottom, record)


def analyze(x11, x22, y11, y22, points, direction, func, record):
    x1, x2, y1, y2 = func(x11, x22, y11, y22)
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        record.append((x1, x2, y1, y2, cur_points, direction))
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})


# 加载数据集
def load():
    res = []
    path = "../Data/{}/Trajectory"
    for i1 in [0, 1, 50, 100, 180]:
        current_path = path.format(str(i1).zfill(3))
        plts = os.scandir(current_path)
        for item in plts:
            path_item = current_path + "\\" + item.name
            with open(path_item, 'r+') as fp:
                for line in fp.readlines()[6::600]:
                    item_list = line.split(',')
                    res.append([float(item_list[0]) + 90, float(item_list[1]) + 180])
    print(len(res))
    return res


def start():
    hil(0, 180, 0, 360, load(), 0)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.ylim(0, 360)
    plt.xlim(0, 180)

    x_list = []
    y_list = []
    for item in curve:
        rectangle = patches.Rectangle((item['x1'], item['y1']), item['x2'] - item['x1'], item['y2'] - item['y1'],
                                      edgecolor='orange', fill=False, linewidth=4)
        ax.add_patch(rectangle)
        rx, ry = rectangle.get_xy()
        cx = rx + rectangle.get_width() / 2.0
        cy = ry + rectangle.get_height() / 2.0
        x_list.append(cx)
        y_list.append(cy)
        ax.annotate(item['index'], (cx, cy), color='black', weight='bold', fontsize=10, ha='center', va='center')

    for i in range(len(x_list) - 1):
        dx = x_list[i + 1] - x_list[i]
        dy = y_list[i + 1] - y_list[i]
        plt.quiver(x_list[i], y_list[i], dx, dy, angles='xy', scale=1.03, scale_units='xy', width=0.005)
    plt.show()


if __name__ == "__main__":
    start()