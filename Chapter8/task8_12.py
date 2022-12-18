def make_sandwich(*add: str) -> None:
    for ele in add:
        print(ele)


make_sandwich('hehe', 'tomato', 'BBQ')
make_sandwich('xixi', 'haha')
make_sandwich('wawa')
