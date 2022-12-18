from collections import OrderedDict

dictionary = OrderedDict()
dictionary['jiejie'] = 'stupid dog'
dictionary['kangkang'] = 'handsome boy'
dictionary['baobao'] = 'beautiful lady'
for name, description in dictionary.items():
    print(name + ':' + description + '.')
dictionary['derrick'] = "kangkang's english name"
dictionary['stupid dog'] = "jiejie's ture name"
for name, description in dictionary.items():
    print(name + ':' + description + '.')
