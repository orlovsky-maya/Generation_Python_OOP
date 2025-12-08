class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def __init__(self, value, start=0):
        super().__init__(start)
        self.value = value


    def inc(self, n=1):
        self.value += n * 2


    def dec(self, n=1):
        self.value = max(self.value - n * 2, 0)



print(issubclass(DoubledCounter, Counter))

# Valid output
# True


counter = Counter(10)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)

# Valid output

# 10
# 16
# 5
# 0
#
counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
# Valid output
# 20
# 32
# 10
# 0