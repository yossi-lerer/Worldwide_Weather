import datetime

def process_weather_data(location, weather):
    data = {
    'search_time': str(datetime.datetime.now()),
    'city': location["city"],
    'state': location["state"],
    'country': location["country"],
    'temperature': weather["main"]["temp"],
    'feels_like': weather["main"]["feels_like"],
    'condition': weather["weather"][0]["description"],
    'humidity': weather["main"]["humidity"],
    'wind_speed': weather["wind"]["speed"]
    }
    return data

def print_weather(weather_result):
    for feild in weather_result:
        if weather_result[feild] != "":
            print(f"{feild}: {weather_result[feild]}")