import math
class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    @property
    def x1(self):
        if (self.b ** 2 - 4 * self.a * self.c) < 0:
            return None
        else:
            x1 = (-self.b - (math.sqrt(self.b ** 2 - 4 * self.a * self.c))) / (2 * self.a)
            return x1

    @property
    def x2(self):
        if (self.b ** 2 - 4 * self.a * self.c) < 0:
            return None
        else:
            x2 = (-self.b + (math.sqrt(self.b ** 2 - 4 * self.a * self.c))) / (2 * self.a)
            return x2

    @property
    def view(self):
        view = f'{self.a}x^2 + {self.b}x + {self.c}'
        return view.replace('+ -', '- ')

    @property
    def coefficients(self) -> tuple:
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, args):
        a, b, c = args
        self.a = a
        self.b = b
        self.c = c

polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)