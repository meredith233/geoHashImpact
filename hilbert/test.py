from matplotlib import pyplot as plt, patches

curve = []


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
    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 1)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 0)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 0)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 3)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})


# 朝右
def hil1(x11, x22, y11, y22, points):
    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 0)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 1)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 1)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 2)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})


# 朝下
def hil2(x11, x22, y11, y22, points):
    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 3)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 2)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 2)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 1)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})


# 朝左
def hil3(x11, x22, y11, y22, points):
    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 2)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = (y11 + y22) / 2
    y2 = y22
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 3)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = x11
    x2 = (x11 + x22) / 2
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 3)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})

    x1 = (x11 + x22) / 2
    x2 = x22
    y1 = y11
    y2 = (y11 + y22) / 2
    cur_points = filter_point(x1, x2, y1, y2, points)
    if len(cur_points) > 1:
        # 多于1个点，继续递归
        hil(x1, x2, y1, y2, cur_points, 0)
    else:
        record = None
        if len(cur_points) > 0:
            record = cur_points[0]
        curve.append({"x1": x1, "x2": x2, "y1": y1, "y2": y2, "poi": record, "index": len(curve)})


# 加载数据集
def load():
    return [[0, 0], [0, 360], [180, 0], [180, 360], [180, 95], [140, 95]]


hil(0, 180, 0, 360, load(), 0)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ylim(0, 360)
plt.xlim(0, 180)
for item in curve:
    rectangle = patches.Rectangle((item['x1'], item['y1']), item['x2'] - item['x1'], item['y2'] - item['y1'], edgecolor='orange',facecolor="green", linewidth=7)
    ax.add_patch(rectangle)
    rx, ry = rectangle.get_xy()
    cx = rx + rectangle.get_width()/2.0
    cy = ry + rectangle.get_height()/2.0
    ax.annotate(item['index'], (cx, cy), color='black', weight='bold', fontsize=10, ha='center', va='center')

plt.show()

