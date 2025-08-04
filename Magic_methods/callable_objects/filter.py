from typing import Callable, Iterable

class Filter:
    def __init__(self, predicate: Callable):
        self.predicate = predicate

    def __call__(self, iterable: Iterable[int]):
        return list(filter(self.predicate, iterable))

leave_even = Filter(lambda x: x % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6]

print(leave_even(numbers))

more_than_five = Filter(lambda x: x > 5)
numbers = [13, 1, 4, 10, 10, 7]

print(more_than_five(numbers))

