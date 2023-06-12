import geo
import utils


def decode_geohash(lat_hash, lon_hash):
    """
    将给定的geohash编码转化为经纬度
    """
    # 经度范围
    lon_range = (-180.0, 180.0)
    # 纬度范围
    lat_range = (-90.0, 90.0)

    for i in range(len(lon_hash)):
        mid = (lon_range[0] + lon_range[1]) / 2
        if lon_hash[i] == "1":
            lon_range = (mid, lon_range[1])
        else:
            lon_range = (lon_range[0], mid)

        mid = (lat_range[0] + lat_range[1]) / 2
        if lat_hash[i] == "1":
            lat_range = (mid, lat_range[1])
        else:
            lat_range = (lat_range[0], mid)

    x1 = lat_range[0]
    y1 = lon_range[0]
    x2 = lat_range[1]
    y2 = lon_range[1]
    return utils.get_area(x1, y1, x2, y2)


num_range = [c for c in range(15, 22)]

x1 = 39.976875
y1 = 116.328848333333
for num in num_range:
    lat, lon = geo.encode_geohash(x1, y1, num)
    print(num, decode_geohash(lat, lon))
