'''
Author: 饕餮
Date: 2022-01-21 16:01:09
version: 
LastEditors: 饕餮
LastEditTime: 2022-01-21 16:45:45
Description: file content
'''
import random
import hashlib
class Tools:
    @staticmethod
    def RandomString(strLength=10):
        seed = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        sa = []
        for i in range(strLength):
            sa.append(random.choice(seed))
        return ''.join(sa)

    @staticmethod
    def StringMd5(strData):
        hash = hashlib.md5()
        hash.update(strData.encode('utf8'))
        return hash.hexdigest()

    @staticmethod
    def RandomNumer(start=1,end=16):
        return random.randint(start,end)
