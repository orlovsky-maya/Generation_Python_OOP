class SuperInt(int):
    def __iter__(self):
        return map(lambda x: SuperInt(abs(SuperInt(x))), str(abs(self)))

    def repeat(self, n=2):
        if self < 0:
            return SuperInt("-" + str(abs(self)) * n)
        else:
            return SuperInt(str(self) * n)

    def to_bin(self):
        return format(self, 'b')

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)
#
# # Sample Input 1:
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.repeat())
print(superint2.repeat(3))

# # Sample Output 1:
# # 1717
# # -171717
#
#  # Sample Input 2:
#
superint1 = SuperInt(17)
superint2 = SuperInt(-17)

print(superint1.to_bin())
print(superint2.to_bin())

# # Sample Output 2:
#
# # 10001
# # -10001
#
# # Sample Input 3:

superint = SuperInt(17)

print(superint.prev())
print(superint.next())

# # Sample Output 3:
#
# # 16
# # 18
#
# Sample Input 4:
#
superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)

# Sample Output 4:
#
# 1 3 3 7
# 2 0 7 7

# Sample Input 5:
superint1 = SuperInt(2023)

for item in superint1:
    print(item, type(item))

# Sample Output 5:
#
# 2 <class '__main__.SuperInt'>
# 0 <class '__main__.SuperInt'>
# 2 <class '__main__.SuperInt'>
# 3 <class '__main__.SuperInt'>

# Sample Input 6:
superint = SuperInt(30)
#
for i in range(10):
    superint = superint.next()
    print(superint)

# Sample Output 6:

# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40