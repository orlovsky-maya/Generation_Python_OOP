class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple) and len(other) == 2:
            x, y = other
            return self.x == x and self.y == y
        return NotImplemented

# a = Vector(1, 2)
# b = Vector(1, 2)
#
# print(a == b)
# print(a != b)
#
# a = Vector(1, 2)
# pair1 = (1, 2)
# pair2 = (3, 4)
# pair3 = (5, 6, 7)
# pair4 = (1, 2, 3, 4)
# pair5 = (1, 4, 3, 2)
#
# print(a == pair1)
# print(a == pair2)
# print(a == pair3)
# print(a == pair4)
# print(a == pair5)

a = Vector(1, 2)
b = Vector(3, 4)
c = Vector(5, 6)

vectors = [a, b, c]
print(vectors)

# TEST_7:
# [Vector(1, 2), Vector(3, 4), Vector(5, 6)]
