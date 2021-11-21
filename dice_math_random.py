from random import randint as ran

class Dice:
    def __init__(self):
        self.sides=6
    def roll_die(self):
        rolling_die=ran(1,6)
        print(f'{rolling_die},{self.sides}')
dieRolling=Dice()

for i in range(1,10+1):
    print(f'{i} ')
    dieRolling.roll_die()

