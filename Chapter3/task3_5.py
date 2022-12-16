import task3_4

print('Unluckily '+task3_4.names[-1] + " yang le,can't arrive,wu wu wu.")
task3_4.names[-1] = "jiejie's photo"
for name in task3_4.names:
    print("I'd like to invite " + name.strip().title() + ' to have dinner!')
