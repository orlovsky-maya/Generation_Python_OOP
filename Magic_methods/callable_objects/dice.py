from random import randrange

class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return randrange(1, self.sides + 1)

kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])

