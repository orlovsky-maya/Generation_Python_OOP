import functools

class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            value = self.func(*args, **kwargs)
        except Exception as e:
            errortype = type(e)
            return (None, errortype)
        return (value, None)


# Входные данные 1
@exception_decorator
def func(x):
    return 2 * x + 1


print(func(1))
print(func('bee'))

# Выходные данные 1

# (3, None)
# (None, <class 'TypeError'>)

# Входные данные 2
@exception_decorator
def f(x, y):
    return x * y


print(f('stepik', 10))
# Выходные данные 2
# ('stepikstepikstepikstepikstepikstepikstepikstepikstepikstepik', None)