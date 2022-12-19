user_name = input("Please input your name")

with open('task10_3.txt', 'w') as file_object:
    file_object.write(user_name.strip())
