class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"До встречи, {self.name}!")

# with Greeter('Кейв'):
#     print('...')

# Valid output
# Приветствую, Кейв!
# ...
# До встречи, Кейв!

with Greeter('Кейв') as greeter:
    print(greeter.name)

# Valid output
# Приветствую, Кейв!
# Кейв
# До встречи, Кейв!