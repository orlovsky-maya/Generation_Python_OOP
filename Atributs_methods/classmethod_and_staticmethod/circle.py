class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diametr):
        radius = diametr / 2
        return cls(radius)


circle = Circle.from_diameter(10)

print(circle.radius)