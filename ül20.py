import requests

# API võtme ja linna nime määramine
city = input("Sisesta soovitud linn: ")
city = city.strip().capitalize()
print("Sinu otsing:", city)
api_key = "044455a5353dad9101a7eaec2721663d"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)