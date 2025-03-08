import yaml
import requests
import tkinter as tk
from tkinter import messagebox

# Load configuration
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

weather_api_key = config['weather_api_key']

def get_weather(location):
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")

# GUI Setup
root = tk.Tk()
root.title("Weather Information")

def show_weather():
    location = location_entry.get()
    try:
        weather_data = get_weather(location)
        weather_info = f"Location: {weather_data['location']['name']}\nTemperature: {weather_data['current']['temp_c']}°C"
        messagebox.showinfo("Weather Info", weather_info)
    except Exception as e:
        messagebox.showerror("Error", str(e))

location_label = tk.Label(root, text="Enter Location:")
location_label.pack(pady=5)
location_entry = tk.Entry(root)
location_entry.pack(pady=5)
weather_button = tk.Button(root, text="Get Weather", command=show_weather)
weather_button.pack(pady=20)

root.mainloop()