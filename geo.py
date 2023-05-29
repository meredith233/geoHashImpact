import constants


def encode_geohash(latitude, longitude, precision=constants.geo_num):
    """
    将给定的经纬度转化为geohash编码
    """
    lon_hash = ""
    lat_hash = ""
    # 经度范围
    lon_range = (-180.0, 180.0)
    # 纬度范围
    lat_range = (-90.0, 90.0)

    while len(lon_hash) < precision:
        # 二分法判断经纬度所属区间
        mid = (lon_range[0] + lon_range[1]) / 2
        if longitude > mid:
            lon_hash += "1"
            lon_range = (mid, lon_range[1])
        else:
            lon_hash += "0"
            lon_range = (lon_range[0], mid)

        mid = (lat_range[0] + lat_range[1]) / 2
        if latitude > mid:
            lat_hash += "1"
            lat_range = (mid, lat_range[1])
        else:
            lat_hash += "0"
            lat_range = (lat_range[0], mid)

    return lat_hash, lon_hash


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
    return (x1+x2)/2, (y1+y2)/2
