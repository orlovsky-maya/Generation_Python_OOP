import keyword


class NonKeyword:
    def __init__(self, name):
        self._name = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._name in obj.__dict__:
            return obj.__dict__[self._name]
        else:
            raise AttributeError("Атрибут не найден")

    def __set__(self, obj, value):
        if value in keyword.kwlist:
            raise ValueError("Некорректное значение")
        else:
            obj.__dict__[self._name] = value


class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)

# Valid output
# Peter

class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

# Valid output
# Атрибут не найден

class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)

# Valid output
# Некорректное значение

class Student:
    name = NonKeyword('name')

print(Student.name.__class__)

# Valid output
# <class '__main__.NonKeyword'>