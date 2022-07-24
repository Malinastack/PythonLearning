from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


six_sided_dice = Die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
six_sided_dice.roll_die()
ten_sided_dice = Die(10)
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()
ten_sided_dice.roll_die()