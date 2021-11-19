# import random
# import json
# import time
# with open("web5.json","r+")as file:
#     data=json.load(file)
# movies=data
# for i in movies:
#     print(i)
#     random_time=random.randint(1,3)
#     path=open("/home/admin123/Desktop/WebScrapping/Folder9"+i["movieName"]+"text","w")
#     file=path.write(str(i))
#     time.sleep(random_time)

import random
import time
import requests
import os
import json
from Task1 import scrape_top_list
t1=scrape_top_list()
with open("web1.json","r+") as file:
    a=json.load(file)
def  txt():
    random_sleep=random.randint(1,3)
    for i in a:
        path="/home/admin123/Desktop/WebScrapping/Folder8"+i["Name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Desktop/WebScrapping/Folder9"+i["Name"]+".json","w")
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()
        time.sleep(random_sleep)
txt()