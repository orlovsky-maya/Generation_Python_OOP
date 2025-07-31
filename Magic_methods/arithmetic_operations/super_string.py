class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            m = len(self.string) / other
            return SuperString(self.string[0:int(m)])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.string):
                return SuperString("")
            else:
                m = len(self.string) - other
                return SuperString(self.string[0:m])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other >= len(self.string):
                return SuperString("")
            else:
                return SuperString(self.string[other:])
        return NotImplemented

s1 = SuperString('bee')
s2 = SuperString('geek')

print(s1 + s2)
print(s2 + s1)


s = SuperString('beegeek')

print(s * 2)
print(3 * s)
print(s / 3)

s = SuperString('beegeek')

print(s << 4)
print(s >> 3)