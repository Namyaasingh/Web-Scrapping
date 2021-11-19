from Task1 import scrape_top_list
import json
file=open("web1.json","r")
data=json.load(file)

def group_by_year(movies):
    emp={}
    for i in data:
        print(i, "i hai")
        movie_list=[]
        year=i["Year"]
        if year not in emp:
            for key in data:
                print(key,"key hai")
                if year==key["Year"]:
                    movie_list.append(key)
            emp[year]=movie_list
   
    with open("web2.json","w+") as file:
        json.dump(emp,file,indent = 4)
        # a=json.dump(emp)
    # return(movie_dict)
group_by_year(scrape_top_list)
dec_arg=group_by_year(scrape_top_list)