import requests
import tkinter as tk

def get_weather():
    city = city_entry.get().strip()
    api_key = "92976e470f54076469aa87b480cdb07f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        result_label.config(text="City could not be found")
        return
    
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    
    result = f"Temperature: {temp} °C\nHumidity: {humidity}%\nWeather: {description.capitalize()}"
    result_label.config(text=result)

root = tk.Tk()
root.title("Weather-App - Today")
root.geometry("300x250")

title_label = tk.Label(root, text="Get Weather Information from: ", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Show", command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()
