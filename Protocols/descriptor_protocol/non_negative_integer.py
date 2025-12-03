# TODO Need to solve the task
class NonNegativeInteger:
    def __init__(self, name, default=None):
        self._name = name
        self._default = default

    def __get__(self, instance, owner):
        print("вызов get")
        # if instance is None:
        # return self
        if self._default in instance.__dict__:
            return instance.__dict__[self._default]
        else:
            raise AttributeError("Атрибут не найден")

    # def __get__(self, instance, owner):
    #     if instance is None:
    #         return self
    #     if self._default in instance.__dict__:
    #         return instance.__dict__[self._default]
    #     else:
    #         if self._default in owner.__dict__:
    #             return owner.__dict__[self._default]
    #         else:
    #             raise AttributeError("Атрибут не найден")

    def __set__(self, instance, value):
        print("вызов set")
        if isinstance(value, int) and value >= 0:
            instance.__dict__[self._default] = value
        else:
            raise ValueError("Некорректное значение")



# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
# student.score = 90
#
# print(student.score)

# Valid output
# 90
class Student:
    score = NonNegativeInteger('score', 0)

student = Student()

print(student.score)
student.score = 0
print(student.score)

# Valid output
# 0
# 0


# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
#
# try:
#     print(student.score)
# except AttributeError as e:
#     print(e)
#
# # Valid output
# # Атрибут не найден
#
#
# class Student:
#     score = NonNegativeInteger('score')
#
# student = Student()
#
# try:
#     student.score = -90
# except ValueError as e:
#     print(e)
#
# # Valid output
# # Некорректное значение