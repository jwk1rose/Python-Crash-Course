import task3_5

print('\n I found a bigger tabel!')
task3_5.task3_4.names.insert(0, 'baobao1')
task3_5.task3_4.names.insert(2, 'kangkang1')
task3_5.task3_4.names.append("jiejie's another photo")
names = task3_5.task3_4.names
for name in names:
    print("I'd like to invite " + name.strip().title() + ' to have dinner!')
