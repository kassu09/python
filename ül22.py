import datetime
import csv
kp= datetime.datetime.now()
print(kp)

print(kp.strftime("%d.%m.%Y %H:%M:%S"))

sp = datetime.datetime(2009,4,16)
vanus_paevades = kp - sp
print(f"Vanus päevades: {vanus_paevades.days}")

vanus_aastates = vanus_paevades.days // 365
print(f"Vanus aastates: {vanus_aastates}")

if vanus_aastates%5==0:
    print("Sul on juubel)")
else:
    print("Sul ei ole juubel!")


faili_nimi = 'rentals.csv'
autode_arv = 0
kliendid = []

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)
    pais = next(csv_lugeja)

    for rida in csv_lugeja:
        # print (rida[1], rida[2])
        autode_arv+= 1
    print(f"Rendide arv kokku: {autode_arv}")
  
    if rida[7] not in kliendid:
        kliendid.append(rida[7])
    print(f"Unikaalseid kliente: {len(kliendid)}")
    
        