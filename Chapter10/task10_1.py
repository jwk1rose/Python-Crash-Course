with open('task10_1.txt') as file_object:
    contents = file_object.read()
    print('1')
    print(contents.strip())
with open('task10_1.txt') as file_object:
    print('2')
    for line in file_object:
        print(line.strip())
with open('task10_1.txt') as file_object:
    print('3')
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
