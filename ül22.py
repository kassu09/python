import datetime
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