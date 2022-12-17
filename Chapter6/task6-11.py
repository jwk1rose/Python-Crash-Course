cities = {
    'shanghai': {
        'country': 'china',
        'population': 10000000,
        'fact': 'native person are rich in china'
    },
    'london': {
        'country': 'England',
        'population': 1000000,
        'fact': 'London tower'
    },
    'chicago': {
        'country': 'American',
        'population': 100000000,
        'fact': 'wind city'
    }
}

for city, description in cities.items():
    for key, value in description.items():
        print(city.__str__() + "'s " + key.__str__() + ' is ' + value.__str__())
