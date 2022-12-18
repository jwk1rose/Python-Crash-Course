def make_shirt(size: str, word: str = 'Hello Python'):
    print('The word is ' + word + ", and it's size is " + size.upper())


make_shirt('XL', 'Hello world')
make_shirt(size='XXL', word='Hello Java')
make_shirt(size='L')
