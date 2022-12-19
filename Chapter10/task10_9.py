try:
    with open('task10_8_3.txt', 'r') as f_object:
        lines1 = f_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines1:
        print(line.strip())

try:
    with open('task10_8_4.txt', 'r') as f_object:
        lines2 = f_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines2:
        print(line.strip()) 