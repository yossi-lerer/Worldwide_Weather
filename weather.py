import requests 

def get_location(city, country, openweathermap_key, state=""):
        res = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={openweathermap_key}", timeout=30).json()
        if res == []:
            return
        geocoding = [res[0]["lat"], res[0]["lon"]]
        return geocoding

def get_weather(lat, lon, openweathermap_key):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweathermap_key}", timeout=30).json()
    return res

def process_weather_data(location, weather):
     pass