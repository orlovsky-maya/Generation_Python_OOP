class Numbers:

    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def get_even(self):
        return list(filter(lambda x: x % 2 == 0, self.numbers))

    def get_odd(self):
        return list(filter(lambda x: x % 2 != 0, self.numbers))


numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())