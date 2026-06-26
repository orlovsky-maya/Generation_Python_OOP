import json

def jsonattr(filename):
    def decorator(cls):
        with open(filename, 'r', encoding='utf8') as file:
            data = json.load(file)
            for key, value in data.items():
                setattr(cls, key, value)
        return cls

    return decorator


# Входные данные1
with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)
# Выходные данные1
# 1
# 2