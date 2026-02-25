def division_with_remainder(iterable, size):
    return tuple(num % size for num in iterable)


class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100):
        iterable = tuple(num % size for num in iterable)
        instance = super().__new__(cls, iterable)
        instance.iterable = iterable
        instance.size = size
        return instance

# Sample Input 1:

modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))

# Sample Output 1:

# (1, 2, 3, 4, 5)
# <class '__main__.ModularTuple'>

# Sample Input 2:
#
modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)

print(modulartuple)

# Sample Output 2:

# (1, 0, 1, 0, 1)

