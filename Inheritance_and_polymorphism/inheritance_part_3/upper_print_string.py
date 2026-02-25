class UpperPrintString(str):
    def __str__(self):
        return f"{super().__str__().upper()}"


s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)

# Valid output
# BEEGEEK
# BEEGEEK

s = UpperPrintString('beegeek')
print(list(s))

# Valid output
# ['b', 'e', 'e', 'g', 'e', 'e', 'k']