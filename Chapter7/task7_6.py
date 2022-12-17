if_quit = False
while not if_quit:
    add = input("what do you want add to your pizza? If enough,please enter 'quit'.")
    if add.strip() == 'quit':
        break
    else:
        print("we will add " + add + 'to your pizza!')
