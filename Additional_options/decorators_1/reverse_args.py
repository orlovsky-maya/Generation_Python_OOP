import functools

# import functools
#
# def reverse_args(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args = reversed(args)
#         return func(*args, **kwargs)
#     return wrapper

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        args = reversed(args)
        value = self.func(*args, **kwargs)
        return value

    import functools

# Входные данные 1
@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))

# Выходные данные 1
# 9
# Входные данные 2
@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))

# Выходные данные 2
# meloncherryapple