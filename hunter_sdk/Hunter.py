'''
Author: 饕餮
Date: 2022-01-21 10:37:56
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 18:04:17
Description: file content
'''
import json
from hunter_sdk.Common.HunterObject import HunterError, HunterObject
from hunter_sdk.HunterApi import HunterApi

class Hunter:
    def __init__(self,configPath='config.json',keyName='Hunter'):
        with open(configPath, 'r') as config_f:
            Config = json.load(config_f)
            HunterConfig = Config[keyName]
            _username = HunterConfig["username"]
            _apikey = HunterConfig["apikey"]
            self.hunterApi = HunterApi(_username,_apikey)

    def Search(self,queryStr,page=1,page_size=10,days=30):
        responseData = self.hunterApi.GetData(queryStr,page,page_size,days)
        hunterObject = HunterObject(responseData)
        if hunterObject.Code != 200:
            errorObject = HunterError(responseData)
            return errorObject
        self.NowPage = page
        self._usePageSize = page_size
        self._useQuery = queryStr
        self._useDays = days
        self.TotalPage = int(hunterObject.Total / 10)
        if self.TotalPage > 10000: 
            self.TotalPage = 10000
        return hunterObject

    def Next(self,page_number=1):
        page = self.NowPage + page_number
        if page > self.TotalPage: page = self.TotalPage
        return self.Search(self._useQuery,page,self._usePageSize,self._useDays)

    def Last(self,page_number=1):
        page = self.NowPage - page_number
        if page < 1: page = 1
        return self.Search(self._useQuery,page,self._usePageSize,self._useDays)