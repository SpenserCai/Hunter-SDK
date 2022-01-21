'''
Author: 饕餮
Date: 2022-01-21 10:37:56
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 11:32:45
Description: file content
'''
import json
from hunter_sdk.Common.HunterObject import HunterObject
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
        responseData = self.hunterApi(queryStr,page,page_size,days)
        hunterObject = HunterObject(responseData)
        return hunterObject