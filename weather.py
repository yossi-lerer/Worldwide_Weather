import requests 
import os
from dotenv import load_dotenv
load_dotenv()

openweathermap_key=os.getenv("OPENWEATHERMAP")

def get_location(city, country, openweathermap_key, state=""):
    if country == "US":
        res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={openweathermap_key}").json()
        geocoding = [res[0]["lat"], res[0]["lon"]]
    else:
        res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={openweathermap_key}").json()
        geocoding = [res[0]["lat"], res[0]["lon"]]
    return geocoding

def get_weather(lat, lon, openweathermap_key):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweathermap_key}")
    return res.json()

get_loc = get_location("Austin", "US", openweathermap_key, "TX")
print(get_weather(get_loc[0], get_loc[1], openweathermap_key))
