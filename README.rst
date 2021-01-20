| 该项目用于将不规范(或者连续)的文本地址进行尽可能的标准化,
  以及对两个地址进行相似度的计算
| 注：该项目为 https://github.com/IceMimosa/geocoding
  项目的Python封装，原项目为Kotlin开发，这里使用\ ``jpype``\ 模块进行了Python封装，方便使用Python方法调用

.. code:: 

   # 地址标准化
   from GeocodingCHN import Geocoding
   text =  '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
   address_nor = Geocoding.normalizing(text)
   print(address_nor)

.. code:: 

   地址相似度计算
   from GeocodingCHN import Geocoding
   text1 = '山东青岛李沧区延川路116号绿城城园东区7号楼2单元802户'
   text2 = '山东青岛李沧区延川路绿城城园东区7-2-802'
   Address_1 = Geocoding.normalizing(text1)
   Address_2 = Geocoding.normalizing(text2)
   similar = Geocoding.similarityWithResult(Address_1, Address_2)
   print(similar)

   # 参数
   # Address1: 地址1, 由 Geocoding.normalizing 方法返回的 Address 类
   # Address2: 地址2, 由 Geocoding.normalizing 方法返回的 Address 类

.. code:: 

   # 添加自定义地址
   from GeocodingCHN import Geocoding
   Geocoding.addRegionEntry(1, 321200000000, "A街道", Geocoding.RegionType.Street)
   test_address = Geocoding.normalizing("江苏泰州A街道")

   # 参数
   # Id: 地址的ID
   # parentId: 地址的父ID, 必须存在
   # name: 地址的名称
   # RegionType: RegionType,地址类型
   # alias: 地址的别名, default=''
