import functools

class type_check:
    def __init__(self, types: list):
        self.types = types

    def __call__(self, fun):
        @functools.wraps(fun)
        def wrapper(*args, **kwargs):
            arg = list(args)
            if all((isinstance(tup[0], tup[1]) for tup in list(zip(arg, self.types)))):
                value = fun(*args, **kwargs)
            else:
                raise TypeError
            return value
        return wrapper


# Входные данные 1
@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))


# Выходные данные 1
# 3


# Входные данные 2
@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))
# Выходные данные 2

# <class 'TypeError'>

# TEST_6:
@type_check([int, int, str])
def add(a, b, c=3):
    return a + b + c


print(add(1, 2, c=5))

# TEST_6:
# 8