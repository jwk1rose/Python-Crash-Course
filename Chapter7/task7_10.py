result = {}
if_continue = True
while if_continue:
    user_name = input("What is your name?")
    user_input = input("IF you can arrival any where you want,where you want most?")
    result[user_name.strip()] = user_input
    if_continue = input("if continue? (Y/N)").upper() == 'Y'
print(result)
