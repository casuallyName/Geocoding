# -*- coding: utf-8 -*-
# @Time     : 2022/5/25 19:10
# @File     : Geocoding.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :
__all__ = ['Geocoding']

import jpype
import re
import os
import warnings

from .model import Address
from .model import RegionType
from .model import Version
from .model import Document
from .model import MatchedResult


class Geocoding:
    def __init__(self, data_class_path='core/region.dat', strict: bool = False, jvm_path: str = None):
        '''

        :param data_class_path:自定义地址文件路径
        :param strict:模式设置
        :param jvm_path:JVM路径
        '''
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
                jpype.JClass('org.bitlap.geocoding.Geocoding')
                warnings.warn("Geocoding 已被创建，正在尝试重新加载（该过程在Windows环境下可能会出现异常）", category=RuntimeWarning)
            except:
                warnings.warn("JVM 已经在运行", category=RuntimeWarning)
            jpype.addClassPath(class_path)
        self._jar_version = '1.3.0'
        self.geocoding = jpype.JClass('org.bitlap.geocoding.GeocodingX')(data_name, strict=strict)
        self.RegionType = RegionType(jpype.JClass('org.bitlap.geocoding.model.RegionType'))

    @property
    def __version__(self):
        return Version(package='v1.4.1', jar=self._jar_version)

    def normalizing(self, address: str) -> Address:
        """
        地址标准化

        :param address: 文本地址
        :return:
        """
        try:
            address_nor_java = self.geocoding.normalizing(str(address))
            return Address(provinceId=address_nor_java.getProvinceId(), province=address_nor_java.getProvince(),
                           cityId=address_nor_java.getCityId(), city=address_nor_java.getCity(),
                           districtId=address_nor_java.getDistrictId(), district=address_nor_java.getDistrict(),
                           streetId=address_nor_java.getStreetId(), street=address_nor_java.getStreet(),
                           townId=address_nor_java.getTownId(), town=address_nor_java.getTown(),
                           villageId=address_nor_java.getVillageId(), village=address_nor_java.getVillage(),
                           road=address_nor_java.getRoad(),
                           roadNum=address_nor_java.getRoadNum(),
                           buildingNum=address_nor_java.getBuildingNum(),
                           text=address_nor_java.getText(),
                           java=address_nor_java
                           )
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

    def similarityWithResult(self, address_1: [Address, str], address_2: [Address, str]) -> MatchedResult:
        """
        地址相似度计算

        :param Address_1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
        :param Address_2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
        :return:
        """

        if type(address_1) == type(address_2) == Address or type(address_1) == type(address_2) == str:
            if type(address_1) == type(address_2) == Address:
                result = self.geocoding.similarityWithResult(address_1.__java__, address_2.__java__)
            else:
                result = self.geocoding.similarityWithResult(address_1, address_2)
        else:
            raise TypeError(
                "similarityWithResult仅支持计算两个 Address 或 text 之间的相似度,但此时输入类型为 {} 和 {} ".format(
                    type(address_1), type(address_2)))

        try:
            return MatchedResult(doc1=Document(terms=result.getDoc1().getTerms(),
                                               termsMap=result.getDoc1().getTermsMap(),
                                               town=result.getDoc1().getTown(),
                                               village=result.getDoc1().getVillage(),
                                               road=result.getDoc1().getRoad(),
                                               roadNum=result.getDoc1().getRoadNum(),
                                               roadNumValue=result.getDoc1().getRoadNumValue(),
                                               ),
                                 doc2=Document(terms=result.getDoc2().getTerms(),
                                               termsMap=result.getDoc2().getTermsMap(),
                                               town=result.getDoc2().getTown(),
                                               village=result.getDoc2().getVillage(),
                                               road=result.getDoc2().getRoad(),
                                               roadNum=result.getDoc2().getRoadNum(),
                                               roadNumValue=result.getDoc2().getRoadNumValue(),
                                               ),
                                 terms=result.getTerms(),
                                 similarity=result.getSimilarity(),
                                 java=result
                                 )
        except:
            pattern = re.compile("similarity=(.*?)\n\)", re.S)
            return MatchedResult(similarity=eval(re.findall(pattern, str(result.toString()))[0]))

    def similarity(self, address_1: [Address, str], address_2: [Address, str]) -> float:
        """
        地址相似度计算

        :param Address_1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
        :param Address_2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
        :return:
        """

        if type(address_1) == type(address_2) == Address or type(address_1) == type(address_2) == str:
            if type(address_1) == type(address_2) == Address:
                result = self.geocoding.similarity(address_1.__java__, address_2.__java__)
            else:
                result = self.geocoding.similarity(address_1, address_2)
        else:
            raise TypeError(
                "similarityWithResult仅支持计算两个 Address 或 text 之间的相似度,但此时输入类型为 {} 和 {} ".format(
                    type(address_1), type(address_2)))
        return result

    def addRegionEntry(self, Id: int, parentId: int, name: str, RegionType: RegionType, alias: str = '',
                       replace: bool = True) -> bool:
        """
        添加自定义地址信息

        :param Id: 地址的ID
        :param parentId: 地址的父ID, 必须存在
        :param name: 地址的名称
        :param RegionType: 地址类型,RegionType,
        :param alias: 地址的别名, default=''
        :param replace: 是否替换旧地址, 当除了[id]之外的字段, 如果相等就替换
        :return:
        """
        try:
            self.geocoding.addRegionEntry(id=Id, parentId=parentId, name=name,
                                          RegionType=RegionType, alias=alias, replace=replace)
            return True
        except:
            return False

    def segment(self, text: str, seg_type: str = 'ik') -> list:
        '''
        分词

        :param text: input
        :param seg_type: ['ik', 'simple', 'smart', 'word']
        :return:
        '''
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

