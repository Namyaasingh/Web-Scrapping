import requests
from bs4 import BeautifulSoup
import json
from Task1 import movie_data
from pprint import pprint
movieurl = "https://www.rottentomatoes.com/m/toy_story_4"
movieName = "toy_story_4"

def movies_detailes(movieName,movieurl):
    url = requests.get(movieurl)
    data = BeautifulSoup(url.text,"html.parser")
    print(data)
    mainDiv = data.find_all("li",class_ = "meta-row clearfix")
    dict1 = {}
    for i in mainDiv:
        a = i.text
        b = a.split(":")
#         # pprint(b)
#         if "\nRating" in b:
#             dict1["Rating"] =  b[1].replace("\n","").strip()
#             # pprint(dict1)
#         elif "\nGenre" in b:
#             ga = b[1].replace("\n                        ","").strip()
#             list1 = []
#             s = ""
#             for i in ga:
#                 if i == ",":
#                     list1.append(s)
#                     s = ""
#                 else:
#                     s += i                
#             dict1["Genre"] = list1
#             # pprint(dict1)
#         elif "\nOriginal Language" in b:
#             dict1["language"] = b[1].replace("\n","").strip()
#             # pprint(dict1)
#         elif "\nDirector" in b:
#             i = 0
#             list2 = []
#             while i < len(b):
#                 if i == 0:
#                     i += 1
#                     continue
#                 list2.append(b[i].replace("\n",""))
#                 i += 1
#             dict1["director"] = list2
#             # pprint(dict1)
#         elif "\nProducer" in b:
#             i = 0
#             list3 = []
#             while i < len(b):
#                 if i == 0:
#                     i += 1
#                     continue
#                 list3.append(b[i].replace("       ","").strip())
#                 i += 1
#             dict1["Producer"] = list3
#             # pprint(dic""
#             for i in ga:
#                 if i == ",":
#                     list1.append(s)
#                     s = ""
#                 else:
#                     s += i                
#             dict1["Genre"]=list1
#         elif "\nRuntime" in b:
#             s = b[1].replace("\n","").strip()
#             h = int(s[0])*60
#             i = 0
#             j = " "
#             while i < len(s):
#                 if s[i] == "h" or s[i] == "m"  or s[i] == " " or i == 0 or s[i] == "M":
#                     i += 1
#                     continue
#                 else:
#                     j += s[i]
#                     i += 1
#                 h += int(j)   
#             dict1["Runtime"] = h
#             dict1["movieName"] = movieName                   
#     with open("web4.json","w+") as file4:
#             json.dump(dict1,file4,indent = 4)
#             return dict1
movies_detailes("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")