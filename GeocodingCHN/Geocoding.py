#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:11
# @Author  : ZhouHang
# @Email   : fjkl@vip.qq.com
# @File    : Geocoding.py
# @Software: PyCharm
import jpype
import re
import os

jpype.startJVM(jpype.getDefaultJVMPath(), "-ea",
               "-Djava.class.path=" + os.path.abspath(__file__).replace('Geocoding.py', 'geocoding.jar'))


class Address(object):
    def __init__(self, provinceId=None, province=None, cityId=None, city=None, districtId=None, district=None,
                 streetId=None, street=None, townId=None, town=None, villageId=None, village=None, road=None,
                 roadNum=None, buildingNum=None, text=None, java=None):
        self.provinceId = int(provinceId) if provinceId else provinceId
        self.province = province
        self.cityId = int(cityId) if cityId else cityId
        self.city = city
        self.districtId = int(districtId) if districtId else districtId
        self.district = district
        self.streetId = int(streetId) if streetId else streetId
        self.street = street
        self.townId = townId
        self.town = town
        self.villageId = villageId if villageId is not None else None
        self.village = village
        self.road = road
        self.roadNum = roadNum
        self.buildingNum = buildingNum
        self.text = text
        self._AddressClass = jpype.JClass('io.patamon.geocoding.model.Address')
        self._java = java if java is not None else self._AddressClass(self.provinceId, self.province, self.cityId,
                                                                      self.city, self.districtId, self.district,
                                                                      self.streetId, self.street, self.townId,
                                                                      self.town,
                                                                      self.villageId, self.village, self.road,
                                                                      self.roadNum, self.buildingNum, self.text)

    def __str__(self):
        return (f"Address(\n\tprovinceId={self.provinceId}, province={self.province}, " +
                f"\n\tcityId={self.cityId}, city={self.city}, " +
                f"\n\tdistrictId={self.districtId}, district={self.district}, " +
                f"\n\tstreetId={self.streetId}, street={self.street}, " +
                f"\n\ttownId={self.townId}, town={self.town}, " +
                f"\n\tvillageId={self.villageId}, village={self.village}, " +
                f"\n\troad={self.road}, " +
                f"\n\troadNum={self.roadNum}, " +
                f"\n\tbuildingNum={self.buildingNum}, " +
                f"\n\ttext={self.text}\n)")

    @property
    def __dict__(self):
        return {
            'provinceId': self.provinceId,
            'province': self.province,
            'cityId': self.cityId,
            'city': self.city,
            'districtId': self.districtId,
            'district': self.district,
            'streetId': self.streetId,
            'street': self.street,
            'townId': self.townId,
            'town': self.town,
            'villageId': self.villageId,
            'village': self.village,
            'road': self.road,
            'roadNum': self.roadNum,
            'buildingNum': self.buildingNum,
            'text': self.text
        }

    @property
    def __java__(self):
        return self._java


class RegionType(object):
    RegionTypeClass = jpype.JClass('io.patamon.geocoding.model.RegionType')
    Undefined = RegionTypeClass.Undefined  # 未定义区域类型
    Country = RegionTypeClass.Country  # 国家
    Province = RegionTypeClass.Province  # 省份
    ProvinceLevelCity1 = RegionTypeClass.ProvinceLevelCity1  # 直辖市 - 与省份并行的一级
    ProvinceLevelCity2 = RegionTypeClass.ProvinceLevelCity2  # 直辖市 - 与城市并行的一级
    City = RegionTypeClass.City  # 地级市
    CityLevelDistrict = RegionTypeClass.CityLevelDistrict  # 省直辖县级市
    District = RegionTypeClass.District  # 县、区
    Street = RegionTypeClass.Street  # 街道乡镇一级
    PlatformL4 = RegionTypeClass.PlatformL4  # 特定平台的4级地址
    Town = RegionTypeClass.Town  # 附加：乡镇
    Village = RegionTypeClass.Village  # 附加：村



def normalizing(address: str):
    """
    地址标准化

    :param address: 文本地址
    :return:
    """
    geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
    address_nor_java = geocoding.normalizing(str(address))
    pattern = re.compile(
        "Address\(\n\tprovinceId=(.*?), province=(.*?), " +
        "\n\tcityId=(.*?), city=(.*?), " +
        "\n\tdistrictId=(.*?), district=(.*?), " +
        "\n\tstreetId=(.*?), street=(.*?), " +
        "\n\ttownId=(.*?), town=(.*?), " +
        "\n\tvillageId=(.*?), village=(.*?), " +
        "\n\troad=(.*?), " +
        "\n\troadNum=(.*?), " +
        "\n\tbuildingNum=(.*?), " +
        "\n\ttext=(.*?)\n\)"
        , re.S)
    try:
        info = re.findall(pattern, str(address_nor_java.toString()))[0]
        info = [None if i == 'null' or i == 'nan' else i for i in info]
        return Address(info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9],
                       info[10], info[11], info[12], info[13], info[14], info[15], address_nor_java)
    except AttributeError:
        return Address


def similarityWithResult(Address_1: Address, Address_2: Address):
    """
    地址相似度计算

    :param Address_1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
    :param Address_2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
    :return:
    """
    geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
    pattern = re.compile("similarity=(.*?)\n\)", re.S)
    if type(Address_1) == type(Address_2) == Address:
        return eval(re.findall(pattern,
                               str(geocoding.similarityWithResult(Address_1.__java__,
                                                                  Address_2.__java__).toString()))[0])
    else:
        raise TypeError(
            "Geocoding.similarityWithResult仅支持计算两个由 Geocoding.normalizing 方法返回的Address类之间的相似度")


def addRegionEntry(Id: int, parentId: int, name: str, RegionType: RegionType, alias=''):
    """
    添加自定义地址信息

    :param Id: 地址的ID
    :param parentId: 地址的父ID, 必须存在
    :param name: 地址的名称
    :param RegionType: 地址类型,RegionType,
    :param alias: 地址的别名, default=''
    :return:
    """
    geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
    try:
        geocoding.addRegionEntry(Id, parentId, name, RegionType, alias)
        return True
    except:
        return False
