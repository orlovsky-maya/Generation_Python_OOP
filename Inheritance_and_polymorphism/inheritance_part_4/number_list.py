# Need to debug the solution
from collections import UserList

def is_item_number(item):
    if not isinstance(item, int) and not isinstance(item, float):
        raise TypeError("Элементами экземпляра класса NumberList должны быть числа")
    return True


class NumberList(UserList):

    def __init__(self, iterable):
        super().__init__(iterable)
        self.result = []
        for item in iterable:
            if is_item_number(item):
                self.result.append(item)

    def __setitem__(self, index, item):
        if is_item_number(item):
            self.data[index] = item

    # def __add__(self, other):
    #     if all(map(is_item_number, other)):
    #         if isinstance(other, type(self)):
    #             self.data.__add__(other)
    #         else:
    #             self.data.__add__(other)

    def __iadd__(self, other):
        if all(map(is_item_number, other)):
            self.data.__iadd__(other)

    def insert(self, index, item):
        if is_item_number(item):
            self.data.insert(index, item)

    def append(self, item):
        if is_item_number(item):
            self.data.append(item)

    def extend(self, other):
        if all(map(is_item_number, other)):
            if isinstance(other, type(self)):
                self.data.extend(other)
            else:
                self.data.extend(item for item in other)


# # Sample Input 1:
#
# numberlist = NumberList([1, 2])
#
# numberlist.append(3)
# numberlist.extend([4, 5])
# numberlist.insert(0, 0)
# print(numberlist)
#
# # Sample Output 1:
# #
# # [0, 1, 2, 3, 4, 5]
# #
# # Sample Input 2:
#
numberlist = NumberList([0, 1.0])
#
numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)
#
# # Sample Output 2:
# #
# # [0, 1, 2, 3, 4, 5]
# #
# # Sample Input 3:
#
# try:
#     numberlist = NumberList(['a', 'b', 'c'])
# except TypeError as error:
#     print(error)
#
# # Sample Output 3:
# #
# # Элементами экземпляра класса NumberList должны быть числа
# #
# # Sample Input 4:
#
# numberlist = NumberList([1, 2, 3])
#
# try:
#     numberlist.append("4")
# except TypeError as error:
#     print(error)
#
# # Sample Output 4:
# #
# # Элементами экземпляра класса NumberList должны быть числа
#


# TEST_5:
# numberlist = NumberList([1, 2])
#
# try:
#     numberlist += [3, '4']
# except TypeError as e:
#     print(e)



# TEST_5:
# Элементами экземпляра класса NumberList должны быть числа

# TEST_6:
# numberlist1 = NumberList([1, 2])
#
# try:
#     numberlist2 = numberlist1 + [3, '4']
# except TypeError as e:
#     print(e)


# TEST_6:
# Элементами экземпляра класса NumberList должны быть числа


# TEST_12:
# numberlist = NumberList([1, 2, 3])
# new_numberlist = numberlist + [4, 5, 6]
# print(new_numberlist)
# print(type(new_numberlist))

# TEST_12:
# [1, 2, 3, 4, 5, 6]
# <class '__main__.NumberList'>
