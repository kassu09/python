# Kirjutage Pythoni skript, mis simuleerib arvu äraarvamise mängu.
# Programm peab esmalt genereerima juhusliku arvu vahemikus 1 -10.
 #Seejärel küsib programm kasutajalt arve, püüdes ära arvata genereeritud arvu. Kasutaja jätkab arvude sisestamist, kuni ta arvab õige arvu ära. Iga kord, kui kasutaja sisestab arvu, peab programm andma tagasisidet, kas pakutud arv on õige või mitte.
 #Pärast õige arvu äraarvamist teavitab programm kasutajat, mitmenda katsega õige arv ära arvati, ja küsib, kas kasutaja soovib mängida uuesti.
 #Kui kasutaja vastab jaatavalt, genereerib programm uue juhusliku arvu ja mäng algab otsast peale.
 #Kui kasutaja otsustab mitte jätkata, tänab programm kasutajat mängus osalemise eest ja kuvab kõik senised tulemused: mitmenda katsega igal korral õige arv ära arvati.
 #Programm peab kasutama while-tsüklit nii arvude sisestamise protsessi juhtimiseks kui ka mängu kordamise otsustamiseks.

#for tsükliga

import random

number = random.randint(1,10)
print("paku number")


for pakkumised in range(1000):
    pakkumine = int(input())    
    if pakkumine < number:
        print("vale")
    elif pakkumine > number:
              print("vale")
    else:
        break
if pakkumine == number:
    print(f"õige, arvasid {pakkumised+1} prooviga")
