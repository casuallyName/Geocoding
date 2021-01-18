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
    text = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    address_nor = Geocoding.normalizing(text)
    print(address_nor)
    # # 输出java原生类型
    address_nor_java = Geocoding.normalizing(text, java_type=True)

    # 地址相似度计算
    text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
    # text1 = Geocoding.normalizing(text1, java_type=True)
    # text2 = Geocoding.normalizing(text2, java_type=True)
    similar = Geocoding.similarityWithResult(text1, text2)
    print(similar)


    # 查看RegionType
    Geocoding.showRegionType()

    # 添加自定义地址
    Geocoding.addRegionEntry(1, 321200000000, "A街", 'Street')
    test_address = Geocoding.normalizing("江苏泰州A街")
    print(test_address)

