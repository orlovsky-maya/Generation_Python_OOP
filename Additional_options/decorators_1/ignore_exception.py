import functools

class ignore_exception:
    def __init__(self, *args):
        self.args = args

    def __call__(self, fu):
        @functools.wraps(fu)
        def wrapper(*args, **kwargs):
            try:
                value = fu(*args, **kwargs)
                return value
            except Exception as e:
                if type(e) in self.args:
                    print(f"Исключение {type(e).__name__} обработано")
                else:
                    raise e
        return wrapper


# Входные данные
@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x

func(0)
func(1)
# Выходные данные
# Исключение ZeroDivisionError обработано

# Входные данные 2
min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))
# Выходные данные 2
# <class 'TypeError'>
