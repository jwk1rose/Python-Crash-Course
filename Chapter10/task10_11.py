import json

number = input("Please inout your favorite number:")
try:
    with open('task10_11_1.json', 'w') as file_object:
        json.dump(number, file_object)
except FileNotFoundError:
    print("file not found")
else:
    print("write success")

try:
    with open('task10_11_1.json', 'r') as file_object:
        get_number = json.load(file_object)
except FileNotFoundError:
    print("file not found")
else:
    print("I got number:" + get_number)
