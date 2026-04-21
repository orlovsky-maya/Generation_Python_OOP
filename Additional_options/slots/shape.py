from functools import total_ordering

@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')
    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f"{self.color} {self.name} ({self.area})"

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return NotImplemented


# Входные данные1
shape = Shape('triangle', 'red', 12)

print(shape.name)
print(shape.color)
print(shape.area)

# Выходные данные1
# triangle
# red
# 12

# Входные данные2
print(Shape('Square', 'Red', 4))
# Выходные данные2
# Red Square (4)

# Входные данные3
print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
# Выходные данные3
# True
# True

# Входные данные4
shape = Shape('triangle', 'red', 12)

try:
    shape.perimeter = 9
except AttributeError:
    print('Error')
# Выходные данные4
# Error