class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, int) or isinstance(value, float):
                self.__dict__[key] = abs(value)
            else:
                self.__dict__[key] = value

# Solution from teacher
# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for name, value in kwargs.items():
#             setattr(self, name, value)
#
#     def __setattr__(self, name, value):
#         if isinstance(value, (int, float)):
#             value = abs(value)
#         object.__setattr__(self, name, value)

point = NonNegativeObject(x=1, y=-2, z=0, color='black')

print(point.x)
print(point.y)
print(point.z)
print(point.color)


point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)