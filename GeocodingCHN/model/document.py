# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:12
# @File     : document.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :

class Document():
    def __init__(self, terms=None, termsMap=None, town=None, village=None, road=None, roadNum=None, roadNumValue=None):
        self.terms = terms
        self.termsMap = termsMap
        self.town = town
        self.village = village
        self.road = road
        self.roadNum = roadNum
        self.roadNumValue = roadNumValue

    def __str__(self):
        return "Document(terms={terms}, town={town}, village={village}, road={road}, roadNum={roadNum}, roadNumValue={roadNumValue})".format(
            terms=self.terms, town=self.town, village=self.village, road=self.road, roadNum=self.roadNum,
            roadNumValue=self.roadNumValue
        )
