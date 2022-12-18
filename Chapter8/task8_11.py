origin_magicians = ['liuqian', 'dave', 'david']


def print_magicians(magicians: list) -> None:
    """
    ...
    :param magicians:
    :return:
    """

    for magician in magicians:
        print(magician)


def make_great(magicians):
    for index in range(len(magicians)):
        magicians[index] += ' the Great.'
    print_magicians(magicians)


make_great(origin_magicians[:])
print("origin_magicians")
print_magicians(origin_magicians)
