class AnyClass:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __str__(self):
        result = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"AnyClass: {', '.join(result)}"

    def __repr__(self):
        result = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"AnyClass({', '.join(result)})"

# any = AnyClass()
#
# print(str(any))
# print(repr(any))

cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))

obj = AnyClass(attr1=10, attr2='beegeek', attr3=True, attr4=[1, 2, 3], attr5=('one', 'two'), attr6=None)

print(str(obj))
print(repr(obj))