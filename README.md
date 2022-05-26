# Geocoding
![Mac](https://img.shields.io/badge/MacOS-pass-success)
![Linux](https://img.shields.io/badge/Linux-pass-success)
![Windows](https://img.shields.io/badge/Windows-bug-red)

[![PypiVersion](https://img.shields.io/badge/pypi-1.4.1-blue)](https://github.com/casuallyName/Geocoding) 
[![JarVersion](https://img.shields.io/badge/jar-1.3.0-blue)](https://github.com/IceMimosa/geocoding) 
![Python wheels](https://img.shields.io/badge/wheels-%E2%9C%93-4c1.svg?longCache=true&style=flat-square&logo=python&logoColor=white)

* 该模块用于将不规范(或者连续)的文本地址进行尽可能的标准化, 以及对两个地址进行相似度的计算
* 该模块为 [IceMimosa/geocoding](https://github.com/IceMimosa/geocoding) 项目的Python封装，原项目为Kotlin开发
* 为方便使用Python方法调用，这里使用Python的`jpype`模块将 [IceMimosa/geocoding](https://github.com/IceMimosa/geocoding) 进行封装,因此该模块需要Java环境的支持(需要添加JAVA_HOME等环境变量)
* `GeocodingCHN`重新加载功能在Windows平台上可能会遇到错误，参考[Jpype Changelog](https://jpype.readthedocs.io/en/latest/CHANGELOG.html) 1.2.0 - 2020-11-29 更新信息。
* 安装命令 `pip install GeocodingCHN`

## 更新信息：
随[原项目](https://github.com/IceMimosa/geocoding)更新jar包,并适配新增功能。 [新增功能](https://github.com/bitlap/geocoding/releases/tag/v1.3.0)：
- [x] `GeocodingCHN.Geocoding`新增参数设定（为适配`org.bitlap.geocoding.GeocodingX`类）
  * 新增`data_class_path`参数，支持自定义地址文件路径，要求该路径为文件绝对路径，默认使用内置地址`core/region.dat`
  * 新增`strict`参数，默认 `False`。当发现没有省和市，且匹配的父项数量等于1时，能成功匹配。
    * `True`: 严格模式，当发现没有省和市，且匹配的父项数量大于1时，返回 `None`
    * `False`: 非严格模式，当发现没有省和市，且匹配的父项数量大于1时，匹配随机一项省和市
  * 新增`jvm_path`，允许设置JVM路径，但要求该路径为文件绝对路径
- [x] `addRegionEntry` 方法新增 `replace` 参数，表示是否替换旧地址，默认为`True`

其他更新：
-[x] 区分 `similarityWithResult` 与 `similarity` 方法，`similarityWithResult` 返回MatchedResult类型结果，`similarity` 返回float类型结果
-[x] 封装分词方法 `segment`

## GeocodingCHN.Geocoding
```python
from GeocodingCHN import Geocoding
geocoding = Geocoding(data_class_path="core/region.dat",
                      strict= False, 
                      jvm_path= None)
```
* data_class_path : 自定义地址文件路径
* strict : 模式设置
* jvm_path : JVM路径

### GeocodingCHN.Geocoding.normalizing
提供地址标准化

`normalizing(address) -> Address`
* address: 文本地址

```python
from GeocodingCHN import Geocoding
geocoding = Geocoding()
text =  '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
address_nor = geocoding.normalizing(text)
print(address_nor)
```
```
Address(
	provinceId=370000000000, province=山东省, 
	cityId=370200000000, city=青岛市, 
	districtId=370213000000, district=李沧区, 
	streetId=0, street=, 
	townId=0, town=, 
	villageId=0, village=, 
	road=延川路, 
	roadNum=116号, 
	buildingNum=7号楼2单元802户, 
	text=绿城城园东区
)
```
### GeocodingCHN.Geocoding.similarityWithResult
地址相似度计算，返回详细结果

`similarityWithResult(Address1:Address, Address2:Address) -> MatchedResult`
* Address1: 地址1, 由 normalizing 方法返回的 Address 类
* Address2: 地址2, 由 normalizing 方法返回的 Address 类
```python
from GeocodingCHN import Geocoding
geocoding = Geocoding()
text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
Address_1 = geocoding.normalizing(text1)
Address_2 = geocoding.normalizing(text2)
print(geocoding.similarityWithResult(Address_1, Address_2))
```
```
MatchedResult(
	doc1=Document(terms=[Term(延川路), Term(116号), Term(7), Term(2), Term(802), Term(绿城), Term(城), Term(园), Term(东区)], town=None, village=None, road=Term(延川路), roadNum=Term(116号), roadNumValue=116), 
	doc2=Document(terms=[Term(延川路), Term(7), Term(2), Term(802), Term(绿城), Term(城), Term(园), Term(东区)], town=None, village=None, road=Term(延川路), roadNum=None, roadNumValue=0), 
	terms=['MatchedTerm(Term(延川路), coord=-1.0, density=-1.0, boost=2.0, tfidf=8.0)', 'MatchedTerm(Term(7), coord=-1.0, density=-1.0, boost=1.0, tfidf=2.0)', 'MatchedTerm(Term(2), coord=-1.0, density=-1.0, boost=1.0, tfidf=2.0)', 'MatchedTerm(Term(802), coord=-1.0, density=-1.0, boost=1.0, tfidf=2.0)', 'MatchedTerm(Term(绿城), coord=1.0, density=1.0, boost=1.0, tfidf=4.0)', 'MatchedTerm(Term(城), coord=1.0, density=1.0, boost=1.0, tfidf=4.0)', 'MatchedTerm(Term(园), coord=1.0, density=1.0, boost=1.0, tfidf=4.0)', 'MatchedTerm(Term(东区), coord=1.0, density=1.0, boost=1.0, tfidf=4.0)'], 
	similarity=0.9473309334313418
)
```
### GeocodingCHN.Geocoding.similarity
地址相似度计算

`similarityWithResult(Address1:Address, Address2:Address)`
* Address1: 地址1, 由 normalizing 方法返回的 Address 类
* Address2: 地址2, 由 normalizing 方法返回的 Address 类
```python
from GeocodingCHN import Geocoding
geocoding = Geocoding()
text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
Address_1 = geocoding.normalizing(text1)
Address_2 = geocoding.normalizing(text2)
print(geocoding.similarity(Address_1, Address_2))
```
```
0.9473309334313418
```

### GeocodingCHN.Geocoding.addRegionEntry 
添加自定义地址

`addRegionEntry(Id, parentId, name, RegionType, alias='', replace=True) -> bool`
* Id: 地址的ID
* parentId: 地址的父ID, 必须存在
* name: 地址的名称
* RegionType: RegionType,地址类型
* alias: 地址的别名, default=''
* replace: 是否替换旧地址, default=True
```python
from GeocodingCHN import Geocoding
geocoding = Geocoding()
geocoding.addRegionEntry(1, 321200000000, "A街道", geocoding.RegionType.Street)
address_nor = geocoding.normalizing("江苏泰州A街道")
print(address_nor)
```
```
Address(
	provinceId=320000000000, province=江苏省, 
	cityId=321200000000, city=泰州市, 
	districtId=321200000000, district=泰州市, 
	streetId=1, street=A街道, 
	townId=0, town=, 
	villageId=0, village=, 
	road=, 
	roadNum=, 
	buildingNum=, 
	text=
)
```
### GeocodingCHN.Geocoding.segment
分词

`segment(text: str, seg_type: str = 'ik') -> list`
* text: 输入
* seg_type: 支持 ['ik', 'simple', 'smart', 'word']，default = 'ik'
```python
from GeocodingCHN import Geocoding
geocoding = Geocoding()
text = '山东青岛李沧区延川路绿城城园东区7-2-802'
print(geocoding.segment(text))
```
```
['山东', '青岛', '李沧区', '延川路', '绿城', '城', '园', '东区', '7-2-802']
```

# 感谢
* 感谢[原作者](https://github.com/IceMimosa/geocoding)的辛苦付出！
* 感谢[原作者](https://github.com/IceMimosa/geocoding)的感谢！
