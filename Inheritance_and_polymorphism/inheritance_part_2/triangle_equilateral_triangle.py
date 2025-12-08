class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


print(issubclass(EquilateralTriangle, Triangle))
# Valid output
# True

triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())
# Valid output
# 12
# 9