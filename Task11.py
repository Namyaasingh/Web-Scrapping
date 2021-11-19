import json
from pprint import pprint
from bs4 import BeautifulSoup
data=open("web5.json","r+")
Data=json.load(data)
# print(Data)
def analyse_movie_genre(Data):
    gener_list=[]
    gener_dict={}
    for i in Data:
        # print(i)
        if "Genre" in i:
            gener=i["Genre"]
            # print(gener)
            # gener_list.append(gener)
            # print(gener_list)
            for j in gener:
                if j not in gener_dict:
                    gener=j
                    gener_dict[j]=1
                else:
                    gener_dict[j]+=1
            else:
                continue
    # print(gener_dict)
    gener_list.append(gener_dict)
    print(gener_list)
    with open("web11.json","w") as  file:
         json.dump(gener_list,file,indent=4)
analyse_movie_genre(Data)