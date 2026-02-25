class LowerString(str):
    def __new__(cls, obj=""):
        instance = super().__new__(cls, str(obj).lower())
        return instance


s1 = LowerString('BEEGEEK')
s2 = LowerString('BeeGeek')

print(s1)
print(s2)
print(s1 == s2)
print(issubclass(LowerString, str))
# Valid output
# beegeek
# beegeek
# True
# True
#
print(LowerString(['Bee', 'Geek']))
print(LowerString({'A': 1, 'B': 2, 'C': 3}))

# Valid output
# ['bee', 'geek']
# {'a': 1, 'b': 2, 'c': 3}

s = LowerString('BeeGeek')

print(s[0], s[3])

# Valid output
# b g

lowerstring = LowerString()
print(type(lowerstring))

# Valid output
# <class '__main__.LowerString'>