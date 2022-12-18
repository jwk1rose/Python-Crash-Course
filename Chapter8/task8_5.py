def describe_city(city: str, country: str = 'China') -> None:
    """
    print city and country
    :param city: city
    :param country: country
    :return: None
    """
    print(city + ' belongs to ' + country)


describe_city('Beijing')
describe_city(city='Shanghai')
describe_city(city='London', country='England')
