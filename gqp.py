import numpy as np


def generate_query_points(num_areas, area_size, min_x, max_x, min_y, max_y):
    """
    在指定的区域内生成查询点
    """
    queries = []
    for i in range(num_areas):
        x = np.random.uniform(min_x, max_x - area_size)
        y = np.random.uniform(min_y, max_y - area_size)
        for j in range(area_size):
            for k in range(area_size):
                queries.append([x + j, y + k])
    return np.array(queries)


def get_true_counts(query_points, true_data):
    """
    获取给定查询点的真实数据数量
    """
    counts = []
    for point in query_points:
        x, y = point
        count = np.sum(
            (true_data[:, 0] >= x) & (true_data[:, 0] < x + 1) & (true_data[:, 1] >= y) & (true_data[:, 1] < y + 1))
        counts.append(count)
    return np.array(counts)


def apply_ldp_responses(queries, true_counts, epsilon):
    """
    使用LDP随机响应对查询结果进行扰动
    """
    beta = np.exp(epsilon) - 1
    perturb_counts = []
    for count in true_counts:
        prob = np.exp(epsilon * count / beta - epsilon / 2) / (
                    np.exp(epsilon * count / beta - epsilon / 2) + np.exp(-epsilon / 2))
        perturb_count = np.random.binomial(count, prob)
        perturb_counts.append(perturb_count)
    perturb_responses = np.array(perturb_counts) - np.array(true_counts)
    return perturb_responses


# 真实的位置数据（x,y坐标）
true_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])

# 定义查询区域的参数
num_areas = 5
area_size = 10
min_x, max_x = 0, 10
min_y, max_y = 0, 10

# 获取随机查询点并在范围计数查询服务中获取真实数据数量
queries = generate_query_points(num_areas, area_size, min_x, max_x, min_y, max_y)
true_counts = get_true_counts(queries, true_data)

# 对查询结果应用LDP随机响应
epsilon = 1.0
perturb_responses = apply_ldp_responses(queries, true_counts, epsilon)

# 计算查询误差并打印输出
query_errors = np.abs(perturb_responses - true_counts) / area_size**2
print("True Counts:   ", true_counts)
print("Perturb Counts:", perturb_responses + true_counts)
print("Errors:        ", query_errors)
print("Average Error: ", np.mean(query_errors))
