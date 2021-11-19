import json
from Task1 import scrape_top_list
from Task4 import movies_detailes
from bs4 import BeautifulSoup
movie=scrape_top_list()
def get_movies_detailes(movie):
    details=[]
    for i in movie:
        b=movies_detailes(i["Name"],i["Url"])
        details.append(b)
        print(details)
    with open("web5.json","w+") as file:
        json.dump(details,file,indent=4)
            # return details
get_movies_detailes(movie)
