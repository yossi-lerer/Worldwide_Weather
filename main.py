from weather import get_location, get_weather
from user_input import user_input_to_search
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    openweathermap_key=os.getenv("OPENWEATHERMAP")

    UserInput = user_input_to_search()
    if type(UserInput) != list:
        print(UserInput)
        exit()
    
    if len(UserInput) == 2:
        lat_and_lon = get_location(UserInput[1], UserInput[0], openweathermap_key)
    else:
        lat_and_lon = get_location(UserInput[2], UserInput[0], openweathermap_key, UserInput[1])
    
    if lat_and_lon != None:
        print(get_weather(lat_and_lon[0], lat_and_lon[1], openweathermap_key))
    else:
        print("Location not found")
main()