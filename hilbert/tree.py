import math

import utils

rangeNum = 5
q_all = rangeNum * (rangeNum + 1) / 2
num = q_all
f = math.ceil(math.log(num, 2))


node = [129.477125, 255.989985]


check = []
for e in [float(x+1)/10 for x in range(10)]:
    m = 2
    ei = (math.pow(m, 1 / 6) - 1) / (math.pow(2, math.fabs(e * math.log(m, 2))) * (math.pow(m, 1 / 6) - math.pow(m, -f / 6)))
    ei = ei/1000
    sumAll = 0.0
    for i in range(300):
        x, y = utils.add_laplace_noise(node[0], node[1], ei)
        sumAll += utils.distance(x, y, node[0], node[1])+25
    check.append(sumAll / 300)

print(check)


