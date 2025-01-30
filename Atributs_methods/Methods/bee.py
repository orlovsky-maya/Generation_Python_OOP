class Bee:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n

bee = Bee(3, 4)
print(bee.x, bee.y)

bee.move_right(3)
print(bee.x, bee.y)

bee.move_up(5)
print(bee.x, bee.y)

bee.move_left(2)
print(bee.x, bee.y)

bee.move_down(10)
print(bee.x, bee.y)