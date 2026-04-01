from collections.abc import Iterable, Iterator


def is_iterable(obj):
    return True if isinstance(obj, Iterable) else False

def is_iterator(obj):
    return True if isinstance(obj, Iterator) else False

# Sample Input 1:
print(is_iterable(123))
print(is_iterable([1, 2, 3]))
print(is_iterable((1, 2, 3)))
print(is_iterable('123'))
print(is_iterable(iter('123')))
print(is_iterable(map(int, '123')))

# Sample Output 1:
#
# False
# True
# True
# True
# True
# True


# Sample Input 2:

print(is_iterator(123))
print(is_iterator([1, 2, 3]))
print(is_iterator((1, 2, 3)))
print(is_iterator('123'))
print(is_iterator(iter('123')))
print(is_iterator(map(int, '123')))

# Sample Output 2:

# False
# False
# False
# False
# True
# True