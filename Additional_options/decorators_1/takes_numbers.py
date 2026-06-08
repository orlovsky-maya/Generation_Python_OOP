import functools
class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Аргументы должны принадлежать типам int или float")
        for arg in kwargs.values():
            if not isinstance(arg, (int, float)):
                raise TypeError("Аргументы должны принадлежать типам int или float")

        value = self.func(*args, **kwargs)
        return value

# Входные данные 1
@takes_numbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))


# Выходные данные 1
# 2
# 2.5
# 3.0
# 3.75


@takes_numbers
def mul(a, b):
    return a * b

# Входные данные 2
try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)

# Выходные данные 2
# Аргументы должны принадлежать типам int или float

# TEST_5:
@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b='2'))
except TypeError as error:
    print(error)


# TEST_5:
# Аргументы должны принадлежать типам int или float

# TEST_8:
@takes_numbers
def mul(a, b=2):
    return a * b


print(mul(1, b=2))

# TEST_8:
# 2
