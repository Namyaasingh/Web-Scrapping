import requests
import json
from bs4 import BeautifulSoup
import os
from Task1 import scrape_top_list
from Task4 import movies_detailes
movies=scrape_top_list
with open("web1.json","r+")as file:
    a=json.load(file)
def num():
    list = []
    for i in a:
        path="/home/admin123/Desktop/WebScrapping/Folder8"+i["Name"]+".text"
        if os.path.exists(path):
            pass
        else :
            create = open("/home/admin123/Desktop/WebScrapping/Folder8"+ i["Name"] + ".text","w")
            url = requests.get(i["Url"])
            create1= create.write(url.text)
            create.close()
num()