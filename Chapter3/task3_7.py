import task3_6

print('yingyingying,the new table cannot arrive in time.I can only invite 2 people to have dinner')
while len(task3_6.names) > 2:
    print(" wuwuwu ,i am sorry to tell you that I can't invite you " + task3_6.names.pop())
for name in task3_6.names:
    print("I'd like to invite " + name.strip().title() + ' to have dinner!')
del task3_6.names[-1]
del task3_6.names[-1]

print(len(task3_6.names))