class CyclicList:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = iterable[:]

    def __getitem__(self, item):
        while item >= len(self.iterable):
            item = item - len(self.iterable)
        return self.iterable[item]

    def __len__(self):
        return len(self.iterable)

    def append(self, item):
        self.iterable.append(item)

    def pop(self, key: int | None=None):
        if key is None:
            result_item = self.iterable[-1]
            del self.iterable[-1]
            return result_item
        else:
            result_item = self.iterable[key]
            del self.iterable[key]
            return result_item


# cyclic_list = CyclicList([1, 2, 3])
#
# for index, elem in enumerate(cyclic_list):
#     if index > 6:
#         break
#     print(elem, end=' ')

# Valid Output:
# 1 2 3 1 2 3 1


# cyclic_list = CyclicList([1, 2, 3])
#
# cyclic_list.append(4)
# print(cyclic_list.pop())
# print(len(cyclic_list))
# print(cyclic_list.pop(0))
# print(len(cyclic_list))

# Valid Output:
# 4
# 3
# 1
# 2

# data = [1, 2, 3, 4, 5]
# cycliclist = CyclicList(data)
# data.extend([6, 7, 8, 9, 10])
#
# count = 0
# for item in cycliclist:
#     if count == 10:
#         break
#     print(item, end=' ')
#     count += 1

# Valid Output:
# 1 2 3 4 5 1 2 3 4 5

cyclic_list = CyclicList()
cyclic_list.append(1)

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')

# Valid Output:
# 1 1 1 1 1 1 1
