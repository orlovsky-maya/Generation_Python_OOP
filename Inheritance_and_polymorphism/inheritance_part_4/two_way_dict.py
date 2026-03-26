from collections import UserDict


class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        self.data.__setitem__(key, value)
        self.data.__setitem__(value, key)




# Sample Input 1:

twowaydict = TwoWayDict({'apple': 1})

twowaydict['banana'] = 2

print(twowaydict['apple'])
print(twowaydict[1])
print(twowaydict['banana'])
print(twowaydict[2])

# Sample Output 1:
#
# 1
# apple
# 2
# banana

# Sample Input 2:

d = TwoWayDict()
d[3] = 8
d[7] = 6
print(d[3], d[8])
print(d[7], d[6])

d.update({9: 7, 8: 2})
print(d[9], d[7])
print(d[8], d[2])
#
# Sample Output 2:
#
# 8 3
# 6 7
# 7 9
# 2 8

