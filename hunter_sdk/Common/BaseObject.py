import json
class BaseObject:
    def __init__(self):
        self.ObjectData = {}

    def TryGetValue(self,key,default=None):
        keyArray = key.split('.')
        keyStr = ""
        #key内容为字典的不存在则返回默认
        if len(keyArray) > 0:
            baseDic = self.ObjectData
            for k in keyArray[0:len(keyArray)]:
                if k not in baseDic.keys():
                    return default
                baseDic = baseDic[k]
        #key栈组装
        for k in keyArray:
            keyStr +="['{0}']".format(k)
        #数据赋值
        return eval("self.ObjectData" + keyStr)

    def SetValue(self,key,value):
        keyArray = key.split('.')
        keyStr = ""
        #key内容为字典的不存在则建立
        if len(keyArray) > 1:
            baseDic = self.ObjectData
            for k in keyArray[0:len(keyArray)-1]:
                if k not in baseDic.keys():
                    baseDic[k] = {}
                baseDic = baseDic[k]
        #key栈组装
        for k in keyArray:
            keyStr +="['{0}']".format(k)
        #数据赋值
        exec("self.ObjectData" + keyStr + "=value")

    def is_json(self,jsonStr):
        try:
            json_object = json.loads(jsonStr)
        except ValueError as e:
            return False
        return True