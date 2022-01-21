<!--
 * @Author: 饕餮
 * @Date: 2022-01-21 10:36:35
 * @version: 
 * @LastEditors: 饕餮
 * @LastEditTime: 2022-01-21 11:41:07
 * @Description: README
-->
# Hunter-SDK
奇安信 Hunter SDK

# Quick Start

## 访问Hunter官网注册账号
https://hunter.qianxin.com/

## 安装SDK
```
pip3 install hunter-sdk
```

## 构建配置文件

config.json
```json
{
    "Hunter":{
        "username":"your name",
        "apikey":"xxxxx"
    }
}
```

## 开始使用
```python
from hunter_sdk.Hunter import Hunter
#第一个参数是配置文件，第二个参数是存储信息的key
hunter = Hunter('config.json','Hunter')
```