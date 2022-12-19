def country_city(country: str, city: str, **population) -> str:
    for key, value in population.items():
        if key == 'population':
            return city.title() + ',' + country.title() + ' - population ' + str(value)
    return city.title() + ',' + country.title()
