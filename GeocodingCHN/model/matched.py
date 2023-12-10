# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:33
# @File     : matched.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.7
# @About    :
from GeocodingCHN.model import Document


class MatchedTerm:
    def __init__(self, term=None, coord=0, density=0, boost=0, tfidf=0):
        # 匹配的词条
        self.term = term
        # 匹配率
        self.coord = coord
        # 稠密度
        self.density = density
        # 权重
        self.boost = boost
        # 特征值 TF - IDF
        self.tfidf = tfidf

    def __str__(self):
        return "MatchedTerm({}, coord={}, density={}, boost={}, tfidf={})".format(
            self.term, self.coord, self.density, self.boost, self.tfidf)

    def __repr__(self):
        return "MatchedTerm({}, coord={}, density={}, boost={}, tfidf={})".format(
            self.term, self.coord, self.density, self.boost, self.tfidf)


class MatchedResult:
    def __init__(self, doc1=None, doc2=None, terms=None, similarity=.0, java=None):
        self.doc1 = doc1
        self.doc2 = doc2
        self.terms = terms
        self.terms = [] if terms is None else [MatchedTerm(term.getTerm(),
                                                              term.getCoord(),
                                                              term.getDensity(),
                                                              term.getBoost(),
                                                              term.getTfidf(),
                                                              )
                                                  for term in terms]
        self.similarity = similarity
        self._java = java

    def __str__(self):
        return "MatchedResult(\n\tdoc1={doc1}, \n\tdoc2={doc2}, \n\tterms={terms}, \n\tsimilarity={similarity}\n)".format(
            doc1=self.doc1, doc2=self.doc2, terms=self.terms, similarity=self.similarity
        )

    def __repr__(self):
        return "MatchedResult(doc1={doc1}, doc2={doc2}, terms={terms}, similarity={similarity})".format(
            doc1=self.doc1, doc2=self.doc2, terms=self.terms, similarity=self.similarity
        )

    @property
    def java_class(self):
        return self._java

    @classmethod
    def from_java(cls, java):
        return cls(doc1=Document.from_java_class(java.getDoc1()) if java.getDoc1() else None,
                   doc2=Document.from_java_class(java.getDoc2()) if java.getDoc2() else None,
                   terms=java.getTerms() if java.getTerms() else [],
                   similarity=None if java.getSimilarity() is None else float(java.getSimilarity()),
                   java=java
                   )
