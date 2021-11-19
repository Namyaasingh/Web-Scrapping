import json 
import requests 
from bs4 import BeautifulSoup

from Task6 import analyse_movies_language
with open("web5.json","r+")as file:
    a=json.load(file)
def analys_movies_directors(a):
    dic={}
    for i in a:
        if "director" in i:
            director=i["director"]
            print(director)
            for j in director:
                if j not in dic:
                    director=j
                    dic[j]=1
                else:
                    dic[j]+=1
            else:
                continue
    # print(dic)
    with open("web7.json","w+")as f1:
        json.dump(dic,f1,indent=5)
analys_movies_directors(a)