class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"Rectangle({self.length}, {self.width})"

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


rectangle = Rectangle(1, 2)

print(str(rectangle))
print(repr(rectangle))

rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)

print(rectangle1)
print(repr(rectangle2))