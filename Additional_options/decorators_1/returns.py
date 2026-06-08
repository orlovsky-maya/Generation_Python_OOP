import functools
class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, self.datatype):
                raise TypeError

            return value
        return wrapper

# Входные данные 1
@returns(int)
def add(a, b):
    return a + b

print(add(1, 2))
# Выходные данные 1
# 3

# Входные данные 2
@returns(int)
def add(a, b):
    return a + b

try:
    print(add('1', '2'))
except Exception as error:
    print(type(error))
# Выходные данные 2
# <class 'TypeError'>