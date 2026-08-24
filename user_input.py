import questionary

def user_input():
    data = []
    
    print("To get weather data")

    country_name = questionary.text("type the country code").ask()
    if country_name.strip() == "":
        return "country code does not recognize text"
    if len(country_name.strip()) != 2:
        return "Country code must contain exactly two characters."
    data.append(country_name.upper())

    if data[0] == "US":
        state_name = questionary.text("type the name of a state").ask()
        if state_name.strip() == "":
            return "state name name does not recognize text"
        if len(state_name.strip()) != 2:
            return "Country code must contain exactly two characters."
        data.append(state_name.upper())
    
    city_name = questionary.text("type the name of a city").ask()
    if city_name.strip() == "":
        return  "country name name name does not recognize text"
    data.append(city_name)

    return data
