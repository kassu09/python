# def eelarve(kylalisi):
#     return kylalisi * 10 + 55
# 
# 
# 
# kutsutud = int(input("Mitu inimest on kutsutud? "))
# tulevad = int(input("Mitu inimest tuleb? "))
# 
# 
# maksimaalne = eelarve(kutsutud)
# minimaalne = eelarve(tulevad)
# 
# 
# print("Maksimaalne eelarve:", maksimaalne, "eurot")
# print("Minimaalne eelarve:", minimaalne, "eurot")


# def tervitus(n):
#     print('Võõrustaja: "Tere!"')
#     print(f"Täna {n}. kord tervitada, mõtiskleb võõrustaja.")
#     print('Külaline: "Tere, suur tänu kutse eest!"')
# 
# 
# 
# arv = int(input("Sisestage külaliste arv: "))
# 
# for i in range(1, arv + 1):
#     tervitus(i)

def pronksikarva_summa(myndid):
    summa = 0
    for m in myndid:
        if m in (1, 2, 5):
            summa += m
    return summa



failinimi = input("Sisesta failinimi: ")

with open(failinimi, "r") as fail:
    myndid = []
    for rida in fail:
        myndid.append(int(rida.strip()))

tulemus = pronksikarva_summa(myndid)

print("Hoiupõrsasse läheb", tulemus, "senti.")

