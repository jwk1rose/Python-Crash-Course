with open('task10_5.txt', 'w') as file_object:
    while True:
        reason = input('why you like python?')
        if reason == 'q':
            break
        file_object.write(reason+'\n')
