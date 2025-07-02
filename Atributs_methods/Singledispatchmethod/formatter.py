from functools import  singledispatchmethod

class Formatter:

     @singledispatchmethod
     @staticmethod
     def format(data):
         raise TypeError('Аргумент переданного типа не поддерживается')

     @format.register(int)
     @staticmethod
     def int_type(data):
         print(f"Целое число: {data}")


     @format.register(float)
     @staticmethod
     def float_type(data):
         print(f"Вещественное число: {data}")

     @format.register(list)
     @staticmethod
     def list_type(data):
         data_str = ", ".join(map(str, data))
         print(f"Элементы списка: {data_str}")


     @format.register(tuple)
     @staticmethod
     def tuple_type(data):
         data_str = ", ".join(map(str, data))
         print(f"Элементы кортежа: {data_str}")

     @format.register(dict)
     @staticmethod
     def dict_type(data):
         data_str = ', '.join(str((k, v)) for k, v in data.items())
         print(f"Пары словаря: {data_str}")


# Formatter.format(1337)
# Formatter.format(20.77)
#
#
# Formatter.format([10, 20, 30, 40, 50])
# Formatter.format(([1, 3], [2, 4, 6]))
#
# Formatter.format({'Cuphead': 1, 'Mugman': 3})
# Formatter.format({1: 'one', 2: 'two'})
# Formatter.format({1: True, 0: False})


try:
    Formatter.format('All them years, Dutch, for this snake?')
except TypeError as e:
    print(e)