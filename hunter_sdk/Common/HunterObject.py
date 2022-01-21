'''
Author: 饕餮
Date: 2021-11-17 13:53:52
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 12:03:17
Description: file content
'''
from typing import List
from hunter_sdk.Common.BaseObject import *

class HunterListItem(BaseObject):
    def __init__(self,jsonData={}):
        self.ObjectData = jsonData

    @property
    def IsRisk(self):
        return self.TryGetValue("is_risk")

    @property
    def Url(self):
        return self.TryGetValue("url")

    @property
    def Ip(self):
        return self.TryGetValue("ip")

    @property
    def Port(self):
        return self.TryGetValue("port")

    @property
    def WebTitle(self):
        return self.TryGetValue("web_title")

    @property
    def Domain(self):
        return self.TryGetValue("domain")

    @property
    def IsRiskProtocol(self):
        return self.TryGetValue("is_risk_protocol")

    @property
    def Protocol(self):
        return self.TryGetValue("protocol")

    @property
    def BaseProtocol(self):
        return self.TryGetValue("base_protocol")

    @property
    def StatusCode(self):
        return self.TryGetValue("status_code")

    @property
    def Component(self):
        return self.TryGetValue("component")

    @property
    def Os(self):
        return self.TryGetValue("os")

    @property
    def Company(self):
        return self.TryGetValue("company")

    @property
    def Number(self):
        return self.TryGetValue("number")

    @property
    def Country(self):
        return self.TryGetValue("country")

    @property
    def Province(self):
        return self.TryGetValue("province")

    @property
    def City(self):
        return self.TryGetValue("city")

    @property
    def UpdatedAt(self):
        return self.TryGetValue("updated_at")

    @property
    def IsWeb(self):
        return self.TryGetValue("is_web")

    @property
    def AsOrg(self):
        return self.TryGetValue("as_org")

    @property
    def Isp(self):
        return self.TryGetValue("isp")

class HunterObject(BaseObject):
    def __init__(self, jsonData):
        self.ObjectData = jsonData

    @property
    def Code(self):
        return self.TryGetValue("code",0)

    @property
    def Message(self):
        return self.TryGetValue("message","")

    @property
    def Total(self):
        return self.TryGetValue("data.total",0)

    @property
    def TotalPage(self):
        return self.TryGetValue("data.total_page",0)

    @property
    def StartTime(self):
        return self.TryGetValue("data.start_time")

    @property
    def EndTime(self):
        return self.TryGetValue("data.end_time")

    @property
    def IsWeb(self):
        return self.TryGetValue("data.is_web")

    @property
    def HunterList(self) -> List[HunterListItem]:
        returnList = []
        tmpList = self.TryGetValue("data.arr")
        for item in tmpList:
            listItem = HunterListItem(item)
            returnList.append(listItem)
        return returnList