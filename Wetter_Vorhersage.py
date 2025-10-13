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
        result_label.config(text="Stadt nicht gefunden!")
        canvas.delete("all")
        return

    # Temperaturen nach Tag reihen
    daily_temps = defaultdict(list)
    for entry in data['list']:
        date_str = entry['dt_txt'].split(" ")[0]  # nur Datum
        daily_temps[date_str].append(entry['main']['temp'])

    week_text = ""
    temps_for_bars = []
    dates_for_bars = []
    for date, temps in daily_temps.items():
        avg_temp = sum(temps)/len(temps)
        description = data['list'][0]['weather'][0]['description'].capitalize()
        week_text += f"{date}: {avg_temp:.1f} °C, {description}\n"
        temps_for_bars.append(avg_temp)
        # Wochentag merken
        weekday = datetime.strptime(date, "%Y-%m-%d").strftime("%a")
        dates_for_bars.append(weekday)

    result_label.config(text=week_text)

    # Balkenanzeige
    canvas.delete("all")
    max_temp = max(temps_for_bars)
    for i, t in enumerate(temps_for_bars):
        height = (t / max_temp) * 150  # skaliert auf 150 Pixel
        # Balken zeichnen
        canvas.create_rectangle(i*40 + 10, 180 - height, i*40 + 40, 180, fill="skyblue")
        # Temperatur über Balken
        canvas.create_text(i*40 + 25, 180 - height - 10, text=f"{t:.0f}°C", font=("Arial", 9))
        # Wochentag unter Balken
        canvas.create_text(i*40 + 25, 185, text=dates_for_bars[i], font=("Arial", 9))

root = tk.Tk()
root.title("Wetter-App - Wochenvorhersage")
root.geometry("350x450")

title_label = tk.Label(root, text="Wetter der Woche", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=25, font=("Arial", 12))
city_entry.pack(pady=5)
city_entry.insert(0, "Wien")

get_button = tk.Button(root, text="Wetter anzeigen", command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

root.mainloop()
