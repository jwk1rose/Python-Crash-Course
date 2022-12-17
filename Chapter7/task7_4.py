if_quit = False
while not if_quit:
    add = input("what do you want add to your pizza? If enough,please enter 'quit'.")
    if add.strip() == 'quit':
        if_quit = True
    else:
        print("we will add " + add + 'to your pizza!')
