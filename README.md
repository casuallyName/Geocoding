# Geocoding
> 该项目用于将不规范(或者连续)的文本地址进行尽可能的标准化, 以及对两个地址进行相似度的计算
> 
> **注：**
> 该项目为 [IceMimosa/geocoding](https://github.com/IceMimosa/geocoding) 项目的Python封装，原项目为Kotlin开发，
> 这里使用`jpype`模块进行了Python封装，方便使用Python方法调用
## 地址标准化
`Geocoding.normalizing(address,java_type=False) `
* address: 文本地址
* java_type: 返回java原生类型,<java class 'io.patamon.geocoding.model.Address'>, default=False
* return: dict
```python
from Geocoding import Geocoding
Geocoding = Geocoding()
text =  '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
address_nor = Geocoding.normalizing(text)
print(address_nor)
```

## 地址相似度计算
`Geocoding.similarityWithResult(Address1, Address2)`
* text1: 地址1, 请确保两个输入参数类型相同， 支持`<class 'str'>`或`<java class 'io.patamon.geocoding.model.Address'>`类型
* text2: 地址2, 请确保两个输入参数类型相同， 支持`<class 'str'>`或`<java class 'io.patamon.geocoding.model.Address'>`类型
* return float
```python
from Geocoding import Geocoding
Geocoding = Geocoding()
text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
similar = Geocoding.similarityWithResult(text1, text2)
print(similar)
```

## 添加自定义地址
`Geocoding.addRegionEntry(Id, parentId, name, RegionType, alias='')`
* Id: 地址的ID
* parentId: 地址的父ID, 必须存在
* name: 地址的名称
* RegionType: RegionType,地址类型, [请在ShowRegionType中查看详细信息]
* alias: 地址的别名, default=''
* return: bool
```python
from Geocoding import Geocoding
Geocoding = Geocoding()
Geocoding.addRegionEntry(1, 321200000000, "A", 'Street')
test_address = Geocoding.normalizing("江苏泰州A")
print(test_address)
```

##  查看RegionType
`Geocoding.showRegionType()`
