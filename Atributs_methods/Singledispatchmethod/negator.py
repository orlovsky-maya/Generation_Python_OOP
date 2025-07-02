from functools import  singledispatchmethod

class Negator:

    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def negative_num(data):
        return data * (-1)

    @neg.register(bool)
    @staticmethod
    def negative_bool(data):
        return not data

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))


try:
    Negator.neg('number')
except TypeError as e:
    print(e)