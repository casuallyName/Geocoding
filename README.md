# Geocoding
> 该模块用于将不规范(或者连续)的文本地址进行尽可能的标准化, 以及对两个地址进行相似度的计算
> 
> **注：**
> 该模块为 [IceMimosa/geocoding](https://github.com/IceMimosa/geocoding) 项目的Python封装，原项目为Kotlin开发
> 
> 为方便使用Python方法调用，这里使用Python的`jpype`模块将 [IceMimosa/geocoding](https://github.com/IceMimosa/geocoding) 进行封装
> 
>因此该模块需要Java环境的支持(需要添加JAVA_HOME等环境变量)
* 安装命令 `pip install GeocodingCHN`
## 地址标准化
`Geocoding.normalizing(address) `
* address: 文本地址
```python
from GeocodingCHN import Geocoding
text =  '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
address_nor = Geocoding.normalizing(text)
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
## 地址相似度计算
`Geocoding.similarityWithResult(Address1, Address2)`
* Address1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
* Address2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类
```python
from GeocodingCHN import Geocoding
text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
Address_1 = Geocoding.normalizing(text1)
Address_2 = Geocoding.normalizing(text2)
similar = Geocoding.similarityWithResult(Address_1, Address_2)
print(similar)
```
```
0.9473309334313418
```
## 添加自定义地址
`Geocoding.addRegionEntry(Id, parentId, name, RegionType, alias='')`
* Id: 地址的ID
* parentId: 地址的父ID, 必须存在
* name: 地址的名称
* RegionType: RegionType,地址类型
* alias: 地址的别名, default=''
* return: bool
```python
from GeocodingCHN import Geocoding
Geocoding.addRegionEntry(1, 321200000000, "A街道", Geocoding.RegionType.Street)
test_address = Geocoding.normalizing("江苏泰州A街道")
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

