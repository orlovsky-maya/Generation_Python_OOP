class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = list(iterable)
        self.n = n
        self.index = -self.n - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += self.n + 1
        if self.index >= len(self.iterable):
            raise StopIteration
        return self.iterable[self.index]


skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)

# # Valid Output:
# # 1 3 5 7 9

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)

# # Valid Output:
# # 1 4 7 10
#

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)
#
# # Valid Output:
# # 1 2 3 4 5 6 7 8 9 10

skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)

# Valid Output:
# 1 7