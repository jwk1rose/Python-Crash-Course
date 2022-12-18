import task8_9

origin_magicians = task8_9.origin_magicians


def make_great(magicians):
    for index in range(len(magicians)):
        magicians[index] += ' the Great.'


make_great(origin_magicians)
print(origin_magicians)
