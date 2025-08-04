class QuadraticPolynomial:
    def __init__(self, a , b ,c):
        self.a = a
        self.b = b
        self.c = c
    def __call__(self, x):
        return self.a * x ** 2 + self.b * x + self.c

func = QuadraticPolynomial(1, 2, 1)

print(func(1))
print(func(2))


func = QuadraticPolynomial(1, 3, 4)

print(func(1))
print(func(2))

