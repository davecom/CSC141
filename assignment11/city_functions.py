def city_str(city_name, country_name, population = None):
    if population != None:
        return f"{city_name}, {country_name} - population {population}"
    return f"{city_name}, {country_name}"