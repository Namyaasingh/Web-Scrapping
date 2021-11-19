import json 
import requests 
from bs4 import BeautifulSoup
with open("web5.json","r+")as f:
    data=json.load(f)
# print(data)
def analyse_movies_language(data):
    dict={}
    for i in data:
        # print(i)
        if "language" in i:
            language=i["language"]
            if language not in dict:
                language=i["language"]
                dict[language]=1
            else:
                dict[language]+=1
        else:
            continue
            # for i in language:
            #     # print(i)
            #     if i not in dict:
            #         dict[i]=1
            #     else:
            #         dict[i]+=1
    # print(dict)
    with open("web6.json","w+") as f1:
        json.dump(dict,f1,indent=4)
analyse_movies_language(data)