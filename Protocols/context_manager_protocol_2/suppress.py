class Suppress:
    def __init__(self, *args):
        self.args = [ex_type for ex_type in args]
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.args:
            self.exception = exc_val
            return True
        return False


with Suppress(NameError):
    print('Этой переменной не существует -->', variable)

print('Завершение программы')

# Valid output
# Завершение программы

with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))

# Valid output
# invalid literal for int() with base 10: 'я число'
# <class 'ValueError'>

with Suppress() as context:
    print('All success!')

print(context.exception)
# Valid output
# All success!
# None