import requests

api_key = "92976e470f54076469aa87b480cdb07f"  

city = input("Gib den Ort ein: ").strip()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != 200:
    print("Stadt nicht gefunden!")
else:
    print(f"Stadt: {data['name']}")
    print(f"Temperatur: {data['main']['temp']} °C")
    print(f"Wetter: {data['weather'][0]['description']}")
    print(f"Luftfeuchtigkeit: {data['main']['humidity']}%")
