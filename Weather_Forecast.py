import requests
import tkinter as tk
from collections import defaultdict
from datetime import datetime

def get_weather():
    city = city_entry.get().strip()
    api_key = "92976e470f54076469aa87b480cdb07f"

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "200":
        result_label.config(text="City could not be found")
        canvas.delete("all")
        return

    daily_temps = defaultdict(list)
    for entry in data['list']:
        date_str = entry['dt_txt'].split(" ")[0]
        daily_temps[date_str].append(entry['main']['temp'])

    week_text = ""
    temps_for_bars = []
    weekdays_for_bars = []

    for date, temps in daily_temps.items():
        avg_temp = sum(temps)/len(temps)
        description = data['list'][0]['weather'][0]['description'].capitalize()
        weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%A") 
        week_text += f"{weekday}: {avg_temp:.1f} °C, {description}\n"
        temps_for_bars.append(avg_temp)
        weekdays_for_bars.append(weekday)

    result_label.config(text=week_text)

    # Balkenanzeige
    canvas.delete("all")
    max_temp = max(temps_for_bars)
    for i, t in enumerate(temps_for_bars):
        height = (t / max_temp) * 150  
        canvas.create_rectangle(i*40 + 10, 180 - height, i*40 + 40, 180, fill="skyblue")
        canvas.create_text(i*40 + 25, 180 - height - 10, text=f"{t:.0f}°C", font=("Arial", 9))
        canvas.create_text(i*40 + 25, 190, text=weekdays_for_bars[i], font=("Arial", 9))  

# Tkinter-Fenster
root = tk.Tk()
root.title("Weather-App - Forecast")
root.geometry("350x500")

title_label = tk.Label(root, text="Weekly Weather", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Show weather", command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

root.mainloop()
