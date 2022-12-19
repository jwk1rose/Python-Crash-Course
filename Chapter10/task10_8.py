try:
    with open('task10_8_1.txt', 'r') as f_object:
        lines1 = f_object.readlines()
    with open('task10_8_2.txt', 'r') as f_object:
        lines2 = f_object.readlines()
except FileNotFoundError:
    print("Please input right file name")
else:
    for line in lines1:
        print(line.strip())
    for line in lines2:
        print(line.strip())
