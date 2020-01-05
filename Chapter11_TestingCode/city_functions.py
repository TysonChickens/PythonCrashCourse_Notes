# 11-1 City, Country function

# def get_city_country(city, country):
#     """Generate a formatted single string of City, Country."""
#     city_country = f"{city}, {country}"
#     return city_country.title()
    

# 11-2 Modify function so it requires a third parameter, population.
# This will purposefully fail test case - population is not optional.

# def get_city_country(city, country, population):
#     """Generate a formatted single string of City, Country."""
#     city_country = f"{city}, {country} - population {population}"
#     return city_country.title()

# Population parameter is optional so it will pass.
def get_city_country(city, country, population=''):
    """Generate a formatted single string of City, Country."""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()