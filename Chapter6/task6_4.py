dictionary = {
    'jiejie': 'stupid dog',
    'kangkang': 'handsome boy',
    'baobao': 'beautiful lady',
}
for name, description in dictionary.items():
    print(name + ':' + description + '.')
dictionary['derrick'] = "kangkang's english name"
dictionary['stupid dog'] = "jiejie's ture name"
for name, description in dictionary.items():
    print(name + ':' + description + '.')
