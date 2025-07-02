from functools import  singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register(int)
    @process.register(float)
    @staticmethod
    def int_or_float(data):
        return data * 2

    @process.register(str)
    @staticmethod
    def string(data):
        return data.upper()

    @process.register(list)
    @staticmethod
    def list(data):
        return sorted(data)

    @process.register(tuple)
    @staticmethod
    def tuple(data):
        return tuple(sorted(data))

print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))