favorite_place = {
    'Eric': ['Ning wave', 'shanghai'],
    'frank': ['beijing', 'nanjing'],
    'Alice': ['lasa'],
}
for name, place_list in favorite_place.items():
    for place in place_list:
        print(name + "'s favorite place is:" + place)
