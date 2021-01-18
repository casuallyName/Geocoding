#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/1/18 13:07
# @Author  : ZhouHang
# @Email   : zhouhang@idataway.com
# @File    : Geocoding.py
# @Software: PyCharm
import jpype
import re
import os


class Geocoding():
    def __init__(self, JVMPath=None):
        # print(os.path.abspath(__file__))
        if JVMPath is None:
            self.JVMPath = jpype.getDefaultJVMPath()
        else:
            self.JVMPath = JVMPath

        self.jarPath = "-Djava.class.path=" + os.path.abspath(__file__).replace('Geocoding.py', 'src\geocoding.jar')
        # self.jarPath = "-Djava.class.path=./src/geocoding.jar"
        # print(self.jarPath)
        jpype.startJVM(self.JVMPath, "-ea", self.jarPath)
        self.geocoding = jpype.JClass('io.patamon.geocoding.Geocoding')
        self._RegionTypeClass = jpype.JClass('io.patamon.geocoding.model.RegionType')
        self._RegionType = {
            'Undefined': self._RegionTypeClass.Undefined,  # 未定义区域类型
            'Country': self._RegionTypeClass.Country,  # 国家
            'Province': self._RegionTypeClass.Province,  # 省份
            'ProvinceLevelCity1': self._RegionTypeClass.ProvinceLevelCity1,  # 直辖市 - 与省份并行的一级
            'ProvinceLevelCity2': self._RegionTypeClass.ProvinceLevelCity2,  # 直辖市 - 与城市并行的一级
            'City': self._RegionTypeClass.City,  # 地级市
            'CityLevelDistrict': self._RegionTypeClass.CityLevelDistrict,  # 省直辖县级市
            'District': self._RegionTypeClass.District,  # 县、区
            'Street': self._RegionTypeClass.Street,  # 街道乡镇一级
            'PlatformL4': self._RegionTypeClass.PlatformL4,  # 特定平台的4级地址
            'Town': self._RegionTypeClass.Town,  # 附加：乡镇
            'Village': self._RegionTypeClass.Village  # 附加：村
        }

    def showRegionType(self):
        RegionType = {
            'KeyWord': 'RegionType',
            'Undefined': '未定义区域类型',
            'Country': '国家',
            'Province': '省份',
            'ProvinceLevelCity1': '直辖市 - 与省份并行的一级',
            'ProvinceLevelCity2': '直辖市 - 与城市并行的一级',
            'City': '地级市',
            'CityLevelDistrict': '省直辖县级市',
            'District': '县 区',
            'Street': '街道乡镇一级',
            'PlatformL4': '特定平台的4级地址',
            'Town': '乡镇',
            'Village': '村'
        }
        flag = True
        for k, v in RegionType.items():
            print('{:<20}| {}'.format(k, v))
            if flag:
                print('{:-<20}┼-{}'.format('', '-' * 15))
                flag = False

    def normalizing(self, address, java_type=False):
        '''
        地址标准化

        :param address: 文本地址
        :param java_type: 返回java原生类型,<java class 'io.patamon.geocoding.model.Address'>, defuat=False
        :return:
        '''
        if java_type:
            return self.geocoding.normalizing(str(address))
        else:
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
                info = re.findall(pattern, str(self.geocoding.normalizing(str(address)).toString()))[0]
                info = [None if i == 'null' or i == 'nan' else i for i in info]

                return {
                    'provinceId': info[0],
                    'province': info[1],
                    'cityId': info[2],
                    'city': info[3],
                    'districtId': info[4],
                    'district': info[5],
                    'streetId': info[6],
                    'street': info[7],
                    'townId': info[8],
                    'town': info[9],
                    'villageId': info[10],
                    'village': info[11],
                    'road': info[12],
                    'roadNum': info[13],
                    'buildingNum': info[14],
                    'text': info[15]
                }
            except AttributeError:
                return {
                    'provinceId': '000000000000',
                    'province': None,
                    'cityId': '000000000000',
                    'city': None,
                    'districtId': '000000000000',
                    'district': None,
                    'streetId': None,
                    'street': None,
                    'townId': None,
                    'town': None,
                    'villageId': None,
                    'village': None,
                    'road': None,
                    'roadNum': None,
                    'buildingNum': None,
                    'text': None
                }

    def similarityWithResult(self, Address1, Address2):
        '''
        地址相似度计算, 包含匹配的所有结果

        :param Address1: 地址1, 请确保两个输入参数类型相同， 支持[<class 'str'> 或 <java class 'io.patamon.geocoding.model.Address'>]类型
        :param Address1: 地址2, 请确保两个输入参数类型相同, 支持[<class 'str'> 或 <java class 'io.patamon.geocoding.model.Address'>]类型
        :return:
        '''
        pattern = re.compile("similarity=(.*?)\n\)", re.S)
        return eval(re.findall(pattern, str(self.geocoding.similarityWithResult(Address1, Address2).toString()))[0])

    def addRegionEntry(self, Id, parentId, name, RegionType, alias=''):
        '''
        设置自定义地址

        :param Id: 地址的ID
        :param parentId: 地址的父ID, 必须存在
        :param name: 地址的名称
        :param RegionType: RegionType,地址类型, [请在ShowRegionType中查看详细信息]
        :param alias: 地址的别名
        :return:
        '''
        try:
            self.geocoding.addRegionEntry(Id, parentId, name, self._RegionType[RegionType], alias)
            return True
        except:
            return False
