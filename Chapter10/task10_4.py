# 1
# while True:
#     user = input("Please input your name.")
#     if user == "q":
#         break
#     print('Hello,' + user)
#     with open('task10_4.txt', 'a') as file_object:
#         file_object.write(user + '\n')


with open('task10_4.txt', 'w') as file_object:
    while True:
        user = input("Please input your name.")
        if user == "q":
            break
        print('Hello,' + user)
        file_object.write(user + '\n')
