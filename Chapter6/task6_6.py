name_list = ['derrick', 'Erick', 'frank', 'curry', 'ruby']
favorite_language = {
    'derrick': 'python',
    'Erick': 'c',
    'Alice': 'Java',
    'Frank': 'C++'
}
for name in name_list:
    if name not in favorite_language.keys():
        print('yingyingying ' + name + ',please write tell us your favorite language.')
    else:
        print('thank you! '+name+'.')
