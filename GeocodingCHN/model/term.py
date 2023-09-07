# -*- coding: utf-8 -*-
# @Time     : 2023/9/7 14:04
# @File     : term.py
# @Author   : Hang Zhou
# @Email    : zhouhang@idataway.com
# @Software : Python 3.7
# @About    :

class Term:
    def __init__(self, text, term_type, idf, ref, java):
        self.text = text
        self.term_type = term_type
        self.idf = idf,
        self.ref = ref
        self._java = java

    def __eq__(self, other):
        return bool(self._java.equals(other))

    def hashCode(self):
        return int(self._java.hashCode())

    def __str__(self):
        return f'Term({self.text})'

    def __repr__(self):
        return f'Term({self.text})'

    @property
    def java_class(self):
        return self._java

    @classmethod
    def from_java_class(cls, java):
        return cls(text=java.getText(), term_type=java.getType(), idf=java.getIdf(), ref=java.getRef(), java=java)
