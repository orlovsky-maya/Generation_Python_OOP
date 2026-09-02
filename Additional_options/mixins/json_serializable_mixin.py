import json


class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

# Входные данные1
class Empty(JsonSerializableMixin):
    pass

obj = Empty()
print(obj.to_json())


# Выходные данные1
# {}

# Входные данные2
class Triangle(JsonSerializableMixin):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

triangle = Triangle(3, 5, 4)
print(triangle.to_json())
# Выходные данные2
# {"a": 3, "b": 5, "c": 4}
