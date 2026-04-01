from collections.abc import Sequence

def change_num(num):
    if num == 1:
        return 0
    else:
        return 1

class BitArray(Sequence):
    def __init__(self, iterable=()):
        self.iterable = list(iterable)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key >= len(self.iterable):
            raise IndexError('Неверный индекс')
        return self.iterable[key]

    def __len__(self):
        return len(self.iterable)

    def __invert__(self):
        return BitArray(list(map(change_num, self.iterable)))

    def __and__(self, value):
        if isinstance(value, BitArray):
            if len(value) == len(self.iterable):
                s = [a & b for a, b in zip(self.iterable, value)]
                return BitArray(s)
            else:
                raise TypeError
        else:
            return NotImplemented

    def __or__(self, value):
        if isinstance(value, BitArray) and len(value) == len(self.iterable):
            s = [a | b for a, b in zip(self.iterable, value)]
            return BitArray(s)
        else:
            return NotImplemented


    def __str__(self):
        if self.iterable is not None:
            return f"{self.iterable}"
        else:
            return None

# Sample Input 1:

bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)


# Sample Output 1:

# [1, 0, 1, 1]
# [0, 1, 0, 0]
# 1
# 0
# 1
# True
# False


 # Sample Input 2:

bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))

# Sample Output 2:
#
# [1, 0, 1, 1] <class '__main__.BitArray'>
# [0, 0, 0, 1] <class '__main__.BitArray'>
# [0, 1, 0, 0] <class '__main__.BitArray'>


# TEST_4:
data = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]

bitarray = BitArray(data)

print(bitarray)
data.extend([0, 0, 1, 0, 1, 1])

print(data)
print(bitarray)


# TEST_4:
# [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
# [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
# [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]


# TEST_7:
bitarray = BitArray()
print(bitarray)

# # TEST_7:
# []