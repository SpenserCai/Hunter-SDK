'''
Author: 饕餮
Date: 2022-01-21 10:38:17
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 11:30:42
Description: file content
'''
'''
Author: 饕餮
Date: 2021-11-17 12:01:47
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 09:30:05
Description: file content
'''
import json
import base64
import requests
import datetime
class HunterApi:
    def __init__(self,username,apikey):
        self.url = "https://hunter.qianxin.com/openApi/search"
        self.username = username
        self.apikey = apikey
    def GetData(self,query_str,page=1,page_size=10,days=30):
        nowTime = datetime.datetime.now()
        requestData = {
            "search":base64.urlsafe_b64encode(query_str.encode("utf-8")).decode(),
            "page":page,
            "page_size":page_size,
            "is_web":"1",
            "end_time":nowTime.strftime("%Y-%m-%d"),
            "start_time":(nowTime - datetime.timedelta(days=days)).strftime("%Y-%m-%d"),
            "username":self.username,
            "api-key":self.apikey
        }
        headerData = {
            "Content-Type": "application/json",
        }
        rep = requests.get(self.url,params=requestData,headers=headerData)
        return json.loads(rep.text)

