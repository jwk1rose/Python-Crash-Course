import json

try:
    with open('task10_12.json','r') as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    input_number = input("please input your favorite number:")
    with open('task10_12.json', 'w') as file_object:
        json.dump(input_number, file_object)
else:
    print("welcome back ,your favorite number is:" + number)
