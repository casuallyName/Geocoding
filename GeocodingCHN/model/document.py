# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:12
# @File     : document.py
# @Author  : CasuallyName
# @Email   : fjkl@vip.qq.com
# @Software : Python 3.7
# @About    :
from GeocodingCHN.model.term import Term


class Document():
    def __init__(self, terms=None, termsMap=None, town=None, village=None, road=None, roadNum=None, roadNumValue=None,
                 java=None):
        self.terms = terms
        self.termsMap = termsMap
        self.town = town
        self.village = village
        self.road = road
        self.roadNum = roadNum
        self.roadNumValue = roadNumValue
        self._java = java

    def __str__(self):
        return "Document(terms={terms}, town={town}, village={village}, road={road}, roadNum={roadNum}, roadNumValue={roadNumValue})".format(
            terms=self.terms, town=self.town, village=self.village, road=self.road, roadNum=self.roadNum,
            roadNumValue=self.roadNumValue
        )

    def __repr__(self):
        return "Document(terms={terms}, town={town}, village={village}, road={road}, roadNum={roadNum}, roadNumValue={roadNumValue})".format(
            terms=self.terms, town=self.town, village=self.village, road=self.road, roadNum=self.roadNum,
            roadNumValue=self.roadNumValue
        )

    def get_term(self, text):
        return self._java.getTerm(text)

    @property
    def to_java(self):
        return self._java

    @classmethod
    def from_java_class(cls, java):
        return cls(terms=[Term.from_java_class(i) for i in java.getTerms()],
                   termsMap=java.getTermsMap(),
                   town=java.getTown(),
                   village=java.getVillage(),
                   road=java.getRoad(),
                   roadNum=java.getRoadNum(),
                   roadNumValue=java.getRoadNumValue(),
                   java=java
                   )
