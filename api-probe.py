import requests

api_key = "92976e470f54076469aa87b480cdb07f"  
city = "Wien"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(data)
