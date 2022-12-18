import task8_7

while True:
    name = input("Please input a singer's name:")
    album = input("please input a album of " + name)
    print(task8_7.make_album(name, album))
    if_continue = input("Continue?(Y/N)").upper()
    if if_continue == 'N':
        break
    else:
        continue
