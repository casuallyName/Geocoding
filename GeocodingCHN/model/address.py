# -*- coding: utf-8 -*-
# @Time     : 2022/5/26 11:08
# @File     : address.py
# @Author   : Zhou Hang
# @Email    : zhouhang@idataway.com
# @Software : Python 3.7
# @About    :
import jpype
class Address(object):
    def __init__(self, provinceId=None, province=None, cityId=None, city=None, districtId=None, district=None,
                 streetId=None, street=None, townId=None, town=None, villageId=None, village=None, road=None,
                 roadNum=None, buildingNum=None, text=None, java=None):
        self.provinceId = int(provinceId) if provinceId else provinceId
        self.province = province
        self.cityId = int(cityId) if cityId else cityId
        self.city = city
        self.districtId = int(districtId) if districtId else districtId
        self.district = district
        self.streetId = int(streetId) if streetId else streetId
        self.street = street
        self.townId = townId
        self.town = town
        self.villageId = villageId if villageId is not None else None
        self.village = village
        self.road = road
        self.roadNum = roadNum
        self.buildingNum = buildingNum
        self.text = text
        self._AddressClass = jpype.JClass('org.bitlap.geocoding.model.Address')
        self._java = java if java is not None else self._AddressClass(self.provinceId, self.province, self.cityId,
                                                                      self.city, self.districtId, self.district,
                                                                      self.streetId, self.street, self.townId,
                                                                      self.town,
                                                                      self.villageId, self.village, self.road,
                                                                      self.roadNum, self.buildingNum, self.text)

    def __repr__(self):
        return (f"Address(provinceId={self.provinceId}, province={self.province}, " +
                f"cityId={self.cityId}, city={self.city}, " +
                f"districtId={self.districtId}, district={self.district}, " +
                f"streetId={self.streetId}, street={self.street}, " +
                f"townId={self.townId}, town={self.town}, " +
                f"villageId={self.villageId}, village={self.village}, " +
                f"road={self.road}, " +
                f"roadNum={self.roadNum}, " +
                f"buildingNum={self.buildingNum}, " +
                f"text={self.text})")

    def __str__(self):
        return (f"Address(\n\tprovinceId={self.provinceId}, province={self.province}, " +
                f"\n\tcityId={self.cityId}, city={self.city}, " +
                f"\n\tdistrictId={self.districtId}, district={self.district}, " +
                f"\n\tstreetId={self.streetId}, street={self.street}, " +
                f"\n\ttownId={self.townId}, town={self.town}, " +
                f"\n\tvillageId={self.villageId}, village={self.village}, " +
                f"\n\troad={self.road}, " +
                f"\n\troadNum={self.roadNum}, " +
                f"\n\tbuildingNum={self.buildingNum}, " +
                f"\n\ttext={self.text}\n)")

    @property
    def __dict__(self):
        return {
            'provinceId': self.provinceId,
            'province': self.province,
            'cityId': self.cityId,
            'city': self.city,
            'districtId': self.districtId,
            'district': self.district,
            'streetId': self.streetId,
            'street': self.street,
            'townId': self.townId,
            'town': self.town,
            'villageId': self.villageId,
            'village': self.village,
            'road': self.road,
            'roadNum': self.roadNum,
            'buildingNum': self.buildingNum,
            'text': self.text
        }

    @property
    def __java__(self):
        return self._java

