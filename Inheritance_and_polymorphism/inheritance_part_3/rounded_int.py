def to_nearest_even(num):
    if num % 2 == 0:
        return num
    else:
        return num + 1


def to_nearest_odd(num):
    if num % 2 == 0:
        return num + 1
    else:
        return num

def rounding(num, even: bool):
    if even:
        return to_nearest_even(num)
    else:
        return to_nearest_odd(num)

class RoundedInt(int):
    def __new__(cls, num, even = True):
        num = rounding(num, even)
        instance = super().__new__(cls, num)
        instance.num = num
        return instance

# Sample Input 1:

print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))

# Sample Output 1:

# 8
# 8
# 7
# 9

# Sample Input 2:

roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))

# Sample Output 2:

# 15
# 9
# 8
# <class '__main__.RoundedInt'>
# <class '__main__.RoundedInt'>
#
