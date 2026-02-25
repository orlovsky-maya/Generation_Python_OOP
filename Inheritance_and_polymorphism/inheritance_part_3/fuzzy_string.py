class FuzzyString(str):
    def __eq__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() == other.lower() and other.lower() == self.lower()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() != other.lower() and other.lower() != self.lower()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() < other.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() > other.lower()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() <= other.lower()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, str | FuzzyString):
            return self.lower() >= other.lower()
        return NotImplemented

    def __contains__(self, other):
        if isinstance(other, str | FuzzyString):
            return other.lower()  in self.lower()
        return NotImplemented




s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('beegeek')

print(s1 == s2)
print(s1 in s2)
print(s2 in s1)
print(s2 not in s1)

# Valid output
# True
# True
# True
# False

s1 = FuzzyString('BeeGeek')
s2 = FuzzyString('bee')

print(s2 in s1)
print(s1 in s2)

# Valid output
# True
# False