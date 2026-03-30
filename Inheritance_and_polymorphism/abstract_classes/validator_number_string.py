from abc import ABC, abstractmethod

class Validator(ABC):
    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        self.validate(value)
        obj.__dict__[self._attr] = value


    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("Устанавливаемое значение должно быть числом")
        if self.minvalue is not None:
            if value < self.minvalue:
                raise ValueError(f"Устанавливаемое число должно быть больше или равно {self.minvalue}")
        if self.maxvalue is not None:
           if value > self.maxvalue:
                raise ValueError(f"Устанавливаемое число должно быть меньше или равно {self.maxvalue}")


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Устанавливаемое значение должно быть строкой")
        if self.minsize is not None:
            if len(value) < self.minsize:
                raise ValueError(f"Длина устанавливаемой строки должна быть больше или равна {self.minsize}")
        if self.maxsize is not None:
            if len(value) > self.maxsize:
                raise ValueError(f"Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}")
        if self.predicate is not None:
            if not self.predicate(value):
                raise ValueError("Устанавливаемая строка не удовлетворяет дополнительным условиям")

#
# # Sample Input 1:

class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)
#
# # Sample Output 1:
#
# # 19
# #
# # Sample Input 2:
#
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)
#
# # Sample Output 2:
# #
# # Устанавливаемое значение должно быть числом
# #
# # Sample Input 3:
#
class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)
#
# # Sample Output 3:
# #
# # Устанавливаемое число должно быть больше или равно 18
# #
# Sample Input 4:

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 101
except ValueError as error:
    print(error)
#
# # Sample Output 4:
# #
# # Устанавливаемое число должно быть меньше или равно 99


# # TEST_5:
# class Student:
    age = Number(18)


student = Student()
student.age = 101
print(student.age)

try:
    student.age = 15
except ValueError as error:
    print(error)


# TEST_5:
# 101
# Устанавливаемое число должно быть больше или равно 18


# TEST_9:
class Person:
    name = String(6, 10)


person = Person()
person.name = 'Андрей'
print(person.name)

person.name = 'Абдурахман'
print(person.name)

# TEST_9:
# Андрей
# Абдурахман


# TEST_11:
class Person:
    name = String(6, 10, predicate=lambda x: x.startswith('А'))


person = Person()

try:
    person.name = 'Василий'
except ValueError as e:
    print(e)


# TEST_11:
# Устанавливаемая строка не удовлетворяет дополнительным условиям

# TEST_17:
class Student:
    age = Number(18, 99)

print(Student.age.__class__)

# TEST_17:
# <class '__main__.Number'>