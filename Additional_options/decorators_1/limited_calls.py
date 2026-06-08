import functools
class MaxCallsException(Exception):
    pass

class limited_calls:
    def __init__(self, n):
        self.n = n
        self.counter = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.counter < self.n:
                value = func(*args, **kwargs)
                self.counter += 1
            else:
                raise MaxCallsException("Превышено допустимое количество вызовов")
            return value
        return wrapper


# Входные данные 1
@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add(1, 2))
except MaxCallsException as e:
    print(e)

# Выходные данные 1
# 3
# 7
# 11
# Превышено допустимое количество вызовов