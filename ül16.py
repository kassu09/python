import os
from datetime import date

print(f"Hello {os.getlogin()}")

print(f"Sinu kataloogi tee: {os.getcwd()}")
today=date.today()
try:
    os.mkdir(str(today))
except:
    print("kataloog juba eksisteerib")

mitu=int(input("Mitu kataloogi tahad teha: "))
for i in range(mitu):
    os.mkdir(str(today)+"/"+str(i+1))
    print(f"kataloogid 1-{mitu} tehtud")


kustuta = input(f"kustuta valikust 1-{mitu}:")
path = os.getcwd()+'\\'+str(today)+'\\' + kustuta
# print(path)
if os.path.isdir(path):
    os.rmdir(path)