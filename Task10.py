import json
import requests
from bs4 import BeautifulSoup
with open("web5.json","r+")as k:
        data=json.load(k)
def analyse_language_and_directors(data):
    Director_list=[]
    dic={}
    for i in data:
        if "director" in i:
            director=i["director"]
            for j in director:
                if j not in dic:
                    director=j
                    dic[j]=1
                else:
                    dic[j]+=1
        else:
            continue
    Director_list.append(dic)
    with open("web10.json","w+")as f1:
        json.dump(Director_list,f1,indent=5)
        return Director_list
 
analyse_language_and_directors(data)