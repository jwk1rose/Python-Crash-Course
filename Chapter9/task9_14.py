from random import randint


class Die:
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        return randint(1, self.side)


die0 = Die()
die2 = Die(10)
die1 = Die(20)

num = 0
while num < 10:
    print('第' + str(num) + '次')
    num += 1
    print("die0=" + str(die0.roll_die()))
    print("die1=" + str(die1.roll_die()))
    print("die2=" + str(die2.roll_die()))
