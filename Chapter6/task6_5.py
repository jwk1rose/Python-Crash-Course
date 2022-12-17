river_country = {
    'nile': 'egypt',
    'yangzi river': 'china',
    'yellow river': 'china',
}
for country in sorted(set(river_country.values())):
    print(country)
for river in sorted(set(river_country.keys())):
    print(river)
