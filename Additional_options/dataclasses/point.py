from dataclasses import dataclass, field

@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False, default=0, compare=False)

    def symmetric_x(self):
        return Point(self.x, -self.y)

    def symmetric_y(self):
        return Point(-self.x, self.y)

    def __post_init__(self):
        if self.x == 0 or self.y == 0:
            self.quadrant = 0
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x < 0 < self.y:
            self.quadrant = 2
        elif self.x < 0 and self.y < 0:
            self.quadrant = 3
        elif self.x > 0 > self.y:
            self.quadrant = 4





# Входные данные1
point = Point()

print(point)
print(point.x)
print(point.y)
print(point.quadrant)

# Выходные данные1
# Point(x=0.0, y=0.0, quadrant=0)
# 0.0
# 0.0
# 0

# Входные данные2
point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())

# Выходные данные2
# Point(x=1.0, y=-2.0, quadrant=4)
# Point(x=-1.0, y=2.0, quadrant=2)

# Входные данные3
point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = Point(3, 4)

print(point1 == point2)
print(point1 == point3)
print(point2 != point3)
# Выходные данные3
# True
# False
# True