import json


def get_stored_username():
    filename = 'task10_13.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name?")
    file_name = 'task10_13.json'
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def great_user():
    username = get_stored_username()
    if username:
        upgrade = input("Are you " + username + '? please (Y/N)') != 'Y'
        if upgrade:
            username = get_new_username()
            print("we will remember you from now" + username)
        else:
            print("welcome back " + username + '!')
    else:
        username = get_new_username()
        print("we will remember you " + username)


great_user()
