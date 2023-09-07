# -*- coding: utf-8 -*-
# @Time     : 2022/5/25 19:10
# @File     : Geocoding.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :
__all__ = ['Geocoding']

import os
import re
import traceback
import warnings
from typing import Union

import jpype

from .model import Address
from .model import Document
from .model import MatchedResult
from .model import RegionType
from .model import Version


class Geocoding:
    def __init__(self, data_class_path='core/region.dat', strict: bool = False, jvm_path: str = None):
        """

        :param data_class_path:自定义地址文件路径
        :param strict:模式设置
        :param jvm_path:JVM路径
        """
        class_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],
                                  'geocoding.jar'
                                  )

        # sep = ';' if os.name == 'nt' else os.pathsep
        if data_class_path != 'core/region.dat':
            if os.path.isabs(data_class_path):
                data_class_dir, data_name = os.path.split(data_class_path)
                class_path = class_path + os.pathsep + data_class_dir
            else:
                raise ValueError("'data_class_path' 参数必须为绝对路径")
        else:
            data_name = data_class_path

        if not jpype.isJVMStarted():
            if jvm_path is None:
                jvm_path = jpype.getDefaultJVMPath()
            if not os.path.isabs(jvm_path):
                raise ValueError("'jvm_path' 参数必须为绝对路径")
            jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=" + class_path)  # classpath=class_paths)#
        else:
            try:
                jpype.JClass('org.bitlap.geocoding.GeocodingX')
                warnings.warn("Geocoding 已被创建，正在尝试重新加载（该过程在Windows环境下可能会出现异常）",
                              category=RuntimeWarning)
            except:
                warnings.warn("JVM 已经在运行", category=RuntimeWarning)
            jpype.addClassPath(class_path)
        self.geocoding = jpype.JClass('org.bitlap.geocoding.GeocodingX')(data_name, strict=strict)
        self.RegionType = RegionType(jpype.JClass('org.bitlap.geocoding.model.RegionType'))

    @property
    def __version__(self):
        return Version(package='v1.4.3', jar='v1.3.1 build 2023.09.07')

    def normalizing(self, address: str) -> Address:
        """
        地址标准化

        :param address: 文本地址
        :return:
        """
        try:
            address_nor_java = self.geocoding.normalizing(str(address))
            return Address.from_java_class(address_nor_java)
        except AttributeError:
            address_nor_java = self.geocoding.normalizing(str(address))
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
                return Address()

    def analyze(self, address: Union[Address, str]):
        """
        将地址进行切分

        :param address:
        :return:
        """
        return Document.from_java_class(self.geocoding.analyze(address if type(address) == str else address.java_class))

    def similarity(self, address_1: [Address, str], address_2: [Address, str]) -> float:
        """
        地址相似度计算

        :param Address_1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
        :param Address_2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
        :return:
        """

        address_1 = self.normalizing(address_1) if type(address_1) == str else address_1
        address_2 = self.normalizing(address_2) if type(address_2) == str else address_2

        result = self.geocoding.similarity(address_1.java_class, address_2.java_class)

        return float(result) if result else None

    def similarityWithResult(self, address_1: [Address, str], address_2: [Address, str]) -> MatchedResult:
        """
        地址相似度计算

        :param Address_1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
        :param Address_2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
        :return:
        """
        address_1 = self.normalizing(address_1) if type(address_1) == str else address_1
        address_2 = self.normalizing(address_2) if type(address_2) == str else address_2

        return MatchedResult.from_java(self.geocoding.similarityWithResult(address_1.java_class, address_2.java_class))

    def match(self, text):
        """
        深度优先匹配符合[text]的地址信息

        :param text:
        :return:
        """
        return self.geocoding.match(text)

    def addRegionEntry(self, Id: int, parentId: int, name: str, region_type: RegionType, alias: str = '',
                       replace: bool = True) -> bool:
        """
        添加自定义地址信息

        :param Id: 地址的ID
        :param parentId: 地址的父ID, 必须存在
        :param name: 地址的名称
        :param region_type: 地址类型,RegionType,
        :param alias: 地址的别名, default=''
        :param replace: 是否替换旧地址, 当除了[id]之外的字段, 如果相等就替换
        :return:
        """
        try:
            self.geocoding.addRegionEntry(Id, parentId, name, region_type, alias, replace)
            return True
        except:
            traceback.print_exc()
            return False

    def segment(self, text: str, seg_type: str = 'ik') -> list:
        """
        分词

        :param text: input
        :param seg_type: ['ik', 'simple', 'smart', 'word']
        :return:
        """
        if seg_type == 'ik':
            seg_class = jpype.JClass('org.bitlap.geocoding.core.segment.IKAnalyzerSegmenter')()
        elif seg_type == 'simple':
            seg_class = jpype.JClass('org.bitlap.geocoding.core.segment.SimpleSegmenter')()
        elif seg_type == 'smart':
            seg_class = jpype.JClass('org.bitlap.geocoding.core.segment.SmartCNSegmenter')()
        elif seg_type == 'word':
            seg_class = jpype.JClass('org.bitlap.geocoding.core.segment.WordSegmenter')()
        else:
            raise AttributeError("'seg_type' 只可以是 ['ik', 'simple', 'smart', 'word'] 中的一种")
        return list(seg_class.segment(text))

    def save(self, path):
        """
        保存dat字典

        :param path:
        :return:
        """
        self.geocoding.save(path)
