class Scales:
    def __init__(self):
        self.right_cup = 0
        self.left_cup = 0

    def add_right(self, massa):
        self.right_cup += massa


    def add_left(self, massa):
        self.left_cup += massa

    def get_result(self):
        if self.right_cup > self.left_cup:
           return 'Правая чаша тяжелее'
        elif self.right_cup < self.left_cup:
            return 'Левая чаша тяжелее'
        else:
            return 'Весы в равновесии'

scales = Scales()

scales.add_right(1)
scales.add_right(1)
scales.add_left(2)

print(scales.get_result())