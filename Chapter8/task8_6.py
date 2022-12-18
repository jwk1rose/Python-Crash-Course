def city_country(city: str, country: str = 'China') -> str:
    """

    :param city:city
    :param country:country
    :return:formatted str
    """
    return '(' + city + ',' + country + ")"


print(city_country('Beijing'))
print(city_country('Shanghai'))
print(city_country('Newyork', 'American'))
