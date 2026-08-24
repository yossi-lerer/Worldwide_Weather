import questionary

def user_input_to_search():
    data =  {
    'city': "",
    'state': "",
    'country': "",        
    }

    print("To get weather data")

    country_name = questionary.text("type the country code").ask()
    if country_name.strip() == "":
        return "country code does not recognize text"
    if len(country_name.strip()) != 2:
        return "Country code must contain exactly two characters."
    data["country"] = country_name.upper().strip()

    if data["country"] == "US":
        state_name = questionary.text("type the name of a state").ask()
        if state_name.strip() == "":
            return "state name name does not recognize text"
        if len(state_name.strip()) != 2:
            return "Country code must contain exactly two characters."
        data["state"] = state_name.upper().strip()
    
    city_name = questionary.text("type the name of a city").ask()
    if city_name.strip() == "":
        return  "country name name name does not recognize text"
    data["city"] = city_name.strip()

    return data
