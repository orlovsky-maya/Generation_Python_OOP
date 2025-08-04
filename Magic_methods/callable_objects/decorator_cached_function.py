class CachedFunction:
    def __init__(self, fun):
        self.fun = fun
        self.cache = {}

    def __call__(self, *args):
        key = tuple(args)
        if key in self.cache:
            return self.cache[key]
        else:
            value = self.fun(*args)
            self.cache[key] = value
            return self.fun(*args)


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(100))


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


slow_fibonacci(5)

for args, value in sorted(slow_fibonacci.cache.items()):
    print(args, value)
