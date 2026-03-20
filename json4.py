# Leia, mitu raamatut ilmus enne 2000. aastat.
#	Leia kõik raamatud, mis pole saadaval.
#	Leia vanim raamat andmestikus.
#	Leia zanr, mida esineb andmetes kõige sagedamini.
#	Leia, mitu raamatut on välja antud pärast aastat 2010.
import json
import requests
url = f"https://metshein.com/kordamine/json/raamatud.json"

# API päringu tegemine
response = requests.get(url)

vanim_aasta = 3000
vanim_raamat = ""
zanr = {}
def sagedamini_esinev(loend):
    return max(set(loend), key=loend.count)


# Vastuse kontrollimine
if response.status_code == 200:
    response = requests.get(url)
# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json() 
    list.append(i)
    for i in data():
        if i['väljaandmise_aasta'] < vanim_aasta:
        vanim_aasta = i['väljaandmise_aasta']
        vanim_raamat = i['pealkiri']
    print (vanim_raamat)
else:
   print(response.status_code)




mitte_saadaval = sum(1 for r in data["raamatud"] if not r["saadavus"])
#print(mitte_saadaval)
