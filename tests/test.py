#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:13
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @File    : test.py
# @Software: PyCharm
from GeocodingCHN import Geocoding
from GeocodingCHN.model import Address

if __name__ == '__main__':
    geocoding = Geocoding()
    # geocoding = Geocoding(data_class_path='core/region.dat')
    print(geocoding.__version__)
    text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
    text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
    address_1 = geocoding.normalizing(text1)
    print(address_1)
    address_2 = geocoding.normalizing(text2)

    print(geocoding.analyze(address_1))
    print(geocoding.analyze(text1))

    print(f"geocoding.similarity(address_1, address_2):{geocoding.similarity(address_1, address_2)}")

    similar = geocoding.similarityWithResult(address_1, address_2)
    print(similar)

    text3 = '江西省南昌市新建县四十里堡镇东艾家庄村100号'
    text4 = '广东省深圳市宝安区四十里堡镇东艾家庄村206号'
    Address_3 = geocoding.normalizing(text3)
    Address_4 = geocoding.normalizing(text4)
    print('-' * 30)
    print(geocoding.similarity(Address_3, Address_4))
    print(geocoding.similarityWithResult(Address_3, Address_4))
    print('-'*30)

    print(geocoding.match('山东青岛李沧区'))


    geocoding.addRegionEntry(1, 321200000000, "A街道", geocoding.RegionType.Street)
    print(geocoding.normalizing("江苏泰州A街道"))
    print(geocoding.segment(text2))
    geocoding.save('A.dat')

    print(Address(
        provinceId=420000000000,
        province='province',
        cityId=420100000000,
        city='city',
        districtId=420106000000,
        district='district',
        streetId=420106003000,
        street='street',
        townId=0,
        town='town',
        villageId=0,
        village='village',
        road='road',
        roadNum='roadNum',
        buildingNum='buildingNum',
        text='text',
    ))

