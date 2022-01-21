import time
from hunter_sdk.Hunter import Hunter
hunter = Hunter('config.json','Hunter')
rep = hunter.Search("ip=180.97.168.79")
print("Page Total:{}".format(hunter.TotalPage))
print("Now Page:{}".format(hunter.NowPage))
print("IP List:")
for t in rep.HunterList:
    print("{}:{}".format(t.Ip,t.Port))
time.sleep(2)
print("----------------------------")
rep = hunter.Next(3)
print("Page Total:{}".format(hunter.TotalPage))
print("Now Page:{}".format(hunter.NowPage))
print("IP List:")
for t in rep.HunterList:
    print("{}:{}".format(t.Ip,t.Port))
time.sleep(2)
print("----------------------------")
rep = hunter.Next(99)
print("Page Total:{}".format(hunter.TotalPage))
print("Now Page:{}".format(hunter.NowPage))
print("IP List:")
for t in rep.HunterList:
    print("{}:{}".format(t.Ip,t.Port))
