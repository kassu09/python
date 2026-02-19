
mehed_kokku = 0
mehed_tootunnid = 0
mehed_palk = 0
naised_kokku = 0
naised_tootunnid = 0
naised_palk = 0

with open("palgad.txt") as fail:
    rida= fail.readlines()
    for i in rida:
        tyk = i.split(",")
    if tyk[3] == "Mees":
        mehed_kokku+=1
        print (mehed_kokku)
    
    #tykeldus = rida.split(",")
    #for r in tykeldus:
    #    print(r, end= " ")