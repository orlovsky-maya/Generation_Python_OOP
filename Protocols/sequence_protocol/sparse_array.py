class SparseArray:
    def __init__(self, default):
        self.default = default
        self.sequence = {}

    def __getitem__(self, item):
        if item in self.sequence:
            return self.sequence.get(item)
        else:
            return self.default

    def __setitem__(self, key, value):
        self.sequence[key] = value


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])

# Valid Output:
# 1000
# 1001
# 0

array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])

# Valid Output:

# Timur
# Arthur
# None