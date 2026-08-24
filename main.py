from weather import get_location, get_weather
from user_input import user_input_to_search
from process_data import process_weather_data, print_weather
from process_csv import create_csv, add_row
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    openweathermap_key=os.getenv("OPENWEATHERMAP")
    filename = "weather_history.csv"

    UserInput = user_input_to_search()
    if type(UserInput) != dict:
        print(UserInput)
        exit()
    
    lat_and_lon = get_location(UserInput["city"], UserInput["country"], openweathermap_key, UserInput["state"])
    
    if lat_and_lon != None:
        get_data = get_weather(lat_and_lon[0], lat_and_lon[1], openweathermap_key)
        processed_data =process_weather_data(UserInput, get_data)
        print_weather(processed_data)
        if os.path.exists(filename):
            print(add_row(filename, processed_data))
        else:
            fields = ['search_time', 'city', 'state', 'country', 'temperature', 'feels_like', 'condition', 'humidity', 'wind_speed']
            create_csv(filename, fields)
            add_row(filename, processed_data)
    else:
        print("Location not found")
main()