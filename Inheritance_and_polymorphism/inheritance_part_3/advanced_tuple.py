from typing import Iterable


class AdvancedTuple(tuple):

    def __add__(self, other):
        if isinstance(other, tuple) or isinstance(other, AdvancedTuple):
            return AdvancedTuple(tuple(self) + other)
        elif isinstance(other, Iterable):
            return AdvancedTuple(tuple(self) + tuple(other))
        else:
            return NotImplemented


    def __radd__(self, other):
        if isinstance(other, tuple) or isinstance(other, AdvancedTuple):
            return AdvancedTuple(other + tuple(self))
        elif isinstance(other, Iterable):
            return AdvancedTuple(tuple(other) + tuple(self))
        else:
            return NotImplemented


# Sample Input 1:
advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)


#  Sample Output 1:
#
# (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# ('a', 'b', 1, 2, 3)

# Sample Input 2:

advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))

#  Sample Output 2:
#
# (1, 2, 3, 4, 5, 6, 7, 8)
# <class '__main__.AdvancedTuple'>