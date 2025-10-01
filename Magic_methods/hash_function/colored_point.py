class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def __repr__(self):
        return f"ColoredPoint({self._x}, {self._y}, '{self._color}')"


    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return (self._x == other._x and
                    self._y == other._y and
                    self._color == other._color)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return (self._x != other._x or
                    self._y != other._y or
                    self._color != other._color)
        return NotImplemented

    def __hash__(self):
        return hash((self._x, self._y, self._color))

point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))
#answers:
#True
#True
#False
#False

