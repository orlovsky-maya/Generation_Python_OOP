class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = start


    def inc(self, num: int | None = None):
        if num is None:
            self.value += 1
        else:
            self.value += num

    def dec(self, num: int | None = None):
        if num is None:
            self.value -= 1
        else:
            self.value -= num
        if self.value < 0:
            self.value = 0

class NonDecCounter(Counter):
    def dec(self, num: int | None = None):
        pass

class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit
        self.value = start

    def inc(self, num: int | None = None):
        if num is None:
            self.value += 1
            if  self.value > self.limit:
                self.value = self.limit
        else:
            self.value += num
            if self.value > self.limit:
                self.value = self.limit


print(issubclass(NonDecCounter, Counter))
print(issubclass(LimitedCounter, Counter))
# valid output
# True
# True

counter = Counter()

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(3)
print(counter.value)
counter.dec(10)
print(counter.value)

# valid output
# 0
# 6
# 2
# 0

counter = NonDecCounter(10)

print(counter.value)
counter.inc()
counter.inc(10)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(50)
print(counter.value)

# valid output
# 10
# 21
# 21
# 21

counter = LimitedCounter()

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)


# valid output

# 0
# 5
# 2
# 10

min()