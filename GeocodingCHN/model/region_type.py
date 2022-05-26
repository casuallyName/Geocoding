# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:09
# @File     : region_type.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :

class RegionType(object):
    def __init__(self, RegionTypeClass):
        self.Undefined = RegionTypeClass.Undefined  # 未定义区域类型
        self.Country = RegionTypeClass.Country  # 国家
        self.Province = RegionTypeClass.Province  # 省份
        self.ProvinceLevelCity1 = RegionTypeClass.ProvinceLevelCity1  # 直辖市 - 与省份并行的一级
        self.ProvinceLevelCity2 = RegionTypeClass.ProvinceLevelCity2  # 直辖市 - 与城市并行的一级
        self.City = RegionTypeClass.City  # 地级市
        self.CityLevelDistrict = RegionTypeClass.CityLevelDistrict  # 省直辖县级市
        self.District = RegionTypeClass.District  # 县、区
        self.Street = RegionTypeClass.Street  # 街道乡镇一级
        self.PlatformL4 = RegionTypeClass.PlatformL4  # 特定平台的4级地址
        self.Town = RegionTypeClass.Town  # 附加：乡镇
        self.Village = RegionTypeClass.Village  # 附加：村

    @staticmethod
    def help():
        print('\n'.join([
            'RegionType 说明:',
            '               Country : 国家',
            '              Province : 省份',
            '    ProvinceLevelCity1 : 直辖市(与省份并行的一级)',
            '    ProvinceLevelCity2 : 直辖市(与城市并行的一级)',
            '                  City : 地级市',
            '     CityLevelDistrict : 省直辖县级市',
            '              District : 县、区',
            '                Street : 街道乡镇一级',
            '            PlatformL4 : 特定平台的4级地址',
            '                  Town : 乡镇(附加)',
            '               Village : 村(附加)',
            '             Undefined : 未定义区域类型',
        ]))

