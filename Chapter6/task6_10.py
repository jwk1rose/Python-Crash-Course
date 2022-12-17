people_num = {
    'Mike': [1, 2],
    'Frank': [3, 4],
    'Alice': [5, 6],
    'Curry': [0, 2],
}

for name, num_list in people_num.items():
    for num in num_list:
        print(name + "'s favorite num is " + num.__str__())
