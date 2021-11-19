from Task2 import dec_arg
import json
with open("web2.json","r+")as f:
    data=json.load(f)
def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        Mod=int(index)%10
        print(Mod)
        decade=int(index)-Mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=1:
                for v in movies[x]:
                    moviedec[i].append(v)

    with open("web3.json","w+") as file:
        json.dump(moviedec,file,indent = 4)
        # a=json.dump(moviedec)
    return(moviedec)
print(group_by_decade(data))
