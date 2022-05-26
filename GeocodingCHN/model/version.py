# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:10
# @File     : version.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :

class Version:
    def __init__(self, package, jar):
        self.package = package
        self.jar = jar

    def __repr__(self):
        return f'Package(GeocodingCHN) version: {self.package}\nSource(geocoding.jar) version: {self.jar}'

    def __str__(self):
        return f'Package(GeocodingCHN) version: {self.package}, Source(geocoding.jar) version: {self.jar}'