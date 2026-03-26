from collections import UserString


class MutableString(UserString):

    def __setitem__(self, i, item):
        data_list = list(self.data)
        data_list[i] = item
        self.data = ''.join(data_list)

    def __delitem__(self, i):
        data_list = list(self.data)
        del data_list[i]
        self.data = ''.join(data_list)

    def lower(self):
        self.data = self.data.lower()

    def upper(self):
        self.data = self.data.upper()

    def sort(self, key=None, reverse=False):
        self.data = ''.join(sorted(self.data, key=key, reverse=reverse))





# Sample Input 1:

mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)

# Sample Output 1:
#
# beegeek
# BEEGEEK
# BEEEEGK
#
# Sample Input 2:

mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

# Sample Output 2:
#
# beegeek
# BeeGeek

