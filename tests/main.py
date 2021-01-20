#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:13
# @Author  : ZhouHang
# @Email   : fjkl@vip.qq.com
# @File    : main.py
# @Software: PyCharm
from GeocodingCHN import Geocoding

if __name__=='__main__':
    text = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    res = Geocoding.normalizing(text)
    print(res)
    text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
    Address_1 = Geocoding.normalizing(text1)
    Address_2 = Geocoding.normalizing(text2)
    similar = Geocoding.similarityWithResult(Address_1, Address_2)
    print(similar)
    Geocoding.addRegionEntry(1, 321200000000, "A街道", Geocoding.RegionType.Street)
    test_address = Geocoding.normalizing("江苏泰州A街道")
    print(test_address)