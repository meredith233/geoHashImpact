import numpy as np
import geopandas as gpd
from statistics import mean
import constants
import utils


def add_laplace_noise(x, y):
    b = 1 / constants.epsilon + 10
    noise_x = np.random.laplace(0, b)
    noise_y = np.random.laplace(0, b)
    return x + noise_x, y + noise_y


def to_xy(lat, lng):
    # 创建一个GeoDataFrame对象
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([lng], [lat]), crs='EPSG:4326')

    # 将GeoDataFrame对象转换为墨卡托投影坐标系
    gdf = gdf.to_crs('EPSG:3857')
    return gdf.geometry.x[0], gdf.geometry.y[0]


def to_lat(x, y):
    # 创建一个GeoDataFrame对象
    gdf = gpd.GeoDataFrame(geometry=gpd.points_from_xy([x], [y]), crs='EPSG:3857')

    # 将GeoDataFrame对象转换为经纬度坐标系
    gdf = gdf.to_crs('EPSG:4326')
    return gdf.geometry.x[0], gdf.geometry.y[0]


dis = []
dis_fin = []


def process(lat, lng):
    x, y = to_xy(lat, lng)
    ox, oy = add_laplace_noise(x, y)
    dis.append(utils.cal_dist(x, y, ox, oy))


def next_step():
    dis_fin.append(mean(dis))


def get_dis():
    return dis_fin
