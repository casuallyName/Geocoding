#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:11
# @Author  : ZhouHang
# @Email   : zhouhang@idataway.com
# @File    : main.py.py
# @Software: PyCharm
from Geocoding import Geocoding

if __name__ == '__main__':
    # 初始化
    Geocoding = Geocoding()

    # 地址标准化
    # text = '广东省河源市源城区中山大道16号华怡小区'
    # text = '两水义成路与紫荆路'
    # address_nor = Geocoding.normalizing(text)
    # print(address_nor)

    # 地址相似度计算
    text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    # text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
    # similar = Geocoding.similarityWithResult(text1, text2)
    # print(similar)

    # 查看RegionType
    # Geocoding.showRegionType()

    # 添加自定义地址
    Geocoding.addRegionEntry(1, 321200000000, "A街", 'Street')
    test_address = Geocoding.normalizing("江苏泰州A街")
    print(test_address)

