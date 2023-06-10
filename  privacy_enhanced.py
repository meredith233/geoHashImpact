import math
import random

import utils

a_min = 0.01
k = 10
m = 10


def to_degrees(ang_rad):
    return ang_rad * 180 / math.pi


def to_radians(ang_deg):
    return ang_deg * math.pi / 180


def loc_find(locX, locY, distance, angle):
    rad_lat = to_radians(locX)
    rad_long = to_radians(locY)
    rad_angle = to_radians(angle)
    rad_ang_distance = distance / 6371.0
    temp1 = math.asin(math.sin(rad_lat) * math.cos(rad_ang_distance) + math.cos(rad_lat)
                      * math.sin(rad_ang_distance) * math.cos(rad_angle))
    p = to_degrees(temp1)
    temp2 = rad_long + math.atan2(math.sin(rad_angle) * math.sin(rad_ang_distance) * math.cos(rad_lat),
                                  math.cos(rad_ang_distance) - math.sin(rad_lat) * math.sin(p))
    q = to_degrees(temp2)
    return p, q


def find_dummy(locP, locQ, locX, locY, r):
    rad_lat1 = to_radians(locP)
    rad_long1 = to_radians(locQ)
    rad_lat2 = to_radians(locX)
    rad_long2 = to_radians(locY)
    temp1 = math.sin(rad_long2 - rad_long1) * math.cos(rad_lat2)
    temp2 = math.cos(rad_lat1) * math.sin(rad_lat2) - (math.sin(rad_lat1)
                                                       * math.cos(rad_lat2) * math.cos(rad_long2 - rad_long1))
    a = (to_degrees(math.atan2(temp1, temp2)) + 360) % 360
    b = to_degrees(2 * math.pi / k)
    dummy_set = []
    for idx in range(k):
        dummy_set.append(loc_find(locP, locQ, r, (a + b * (idx + 1))))
    random.shuffle(dummy_set)
    return dummy_set


def start(posX, posY):
    r = math.sqrt(a_min / math.pi)
    st = to_degrees(2 * math.pi / m)
    print(st)
    list1 = []
    for i in range(1, m + 1):
        list1.append(st * i)
    random.shuffle(list1)
    for i in range(1, m + 1):
        p, q = loc_find(posX, posY, r, list1[i])
        dummy_set = find_dummy(p, q, posX, posY, r)
        return dummy_set


x = 31
y = 120
ans = start(x, y)

total = 0.0
for t in ans:
    total += utils.distance(x, y, t[0], t[1])
print(total / len(ans))
