import time
from typing import Any
from hunter_sdk.Common.HunterObject import HunterError, HunterObject
from hunter_sdk.Hunter import Hunter

def ShowData(repObj) -> None:
    if type(repObj) is not HunterError:
        print("Page Total:{}".format(hunter.TotalPage))
        print("Now Page:{}".format(hunter.NowPage))
        print("IP List:")
        for t in repObj.HunterList:
            print("{}:{}".format(t.Ip,t.Port))
        print("----------------------------")
    else:
        print(repObj.ErrorMessage)

hunter = Hunter('config.json','Hunter')

rep = hunter.Search("ip=180.97.168.79")
ShowData(rep)

rep = hunter.Next(3)
ShowData(rep)
time.sleep(5)

rep = hunter.Next(99)
ShowData(rep)
