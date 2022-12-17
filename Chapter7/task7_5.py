if_continue = True
while if_continue:
    age = input('Please tell us your age,and we will charge via your input')
    if int(age.strip()) < 0:
        print('Ghost is not welcomed!')
        if_continue = False
    elif int(age.strip()) < 3:
        print('You are free')
    elif int(age.strip()) < 12:
        print('you need pay 10 dollars')
    else:
        print('you need pay 15 dollars')
