#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:13
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @File    : test.py
# @Software: PyCharm
from GeocodingCHN import Geocoding

if __name__ == '__main__':
    geocoding = Geocoding()
    geocoding = Geocoding(data_class_path='core/region.dat')
    print(geocoding.__version__)
    text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
    Address_1 = geocoding.normalizing(text1)
    print(Address_1)
    Address_2 = geocoding.normalizing(text2)
    similar = geocoding.similarityWithResult(Address_1, Address_2)
    print(similar)
    print(similar.similarity)
    print(geocoding.similarity(Address_1, Address_2))

    geocoding.addRegionEntry(1, 321200000000, "A街道", geocoding.RegionType.Street)
    print(geocoding.normalizing("江苏泰州A街道"))
    print(geocoding.segment(text2))
