current_users = ['derrick', 'baobao', 'jiejie', 'baba', 'mama']
new_users = ['Derrick', 'frank', 'eric', 'alice', 'henry']
for user in new_users:
    if user.lower() in current_users:
        print('Sorry, this id has been already engaged')
    else:
        print('Hello,' + user)
