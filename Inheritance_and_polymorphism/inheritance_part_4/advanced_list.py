class AdvancedList(list):
    def join(self, separator=" "):
        return separator.join(map(str, self))

    def map(self, func):
        self[:] = list(map(func, self))
        return self

    def filter(self, func):
        self[:] = list(filter(func, self))
        return self





# Sample Input 1:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

print(advancedlist.join())
print(advancedlist.join('-'))

# Sample Output 1:
#
# 1 2 3 4 5
# 1-2-3-4-5
#
# Sample Input 2:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)

# Sample Output 2:
#
# [-1, -2, -3, -4, -5]
#
# Sample Input 3:

advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.filter(lambda x: x % 2 == 0)

print(advancedlist)

# Sample Output 3:
#
# [2, 4]
#
# Sample Input 4:

advancedlist = AdvancedList([0, 1, 2, '', 3, (), 4, 5, False, {}])
id1 = id(advancedlist)

advancedlist.filter(bool)
id2 = id(advancedlist)

print(advancedlist)
print(id1 == id2)

# Sample Output 4:
#
# [1, 2, 3, 4, 5]
# True

