class OrderedSet:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = list()
        else:
            self.iterable = list(dict.fromkeys(iterable))

    def __len__(self):
        return len(self.iterable)

    def __contains__(self, item):
        return item in self.iterable

    def __iter__(self):
        yield from self.iterable

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return (self.iterable == other.iterable
                    and len(self.iterable) == len(other.iterable))
        elif isinstance(other, set):
            return (set(self.iterable) == other
                    and len(self.iterable) == len(other))
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, OrderedSet):
            return (self.iterable != other.iterable
                    or len(self.iterable) == len(other.iterable))
        elif isinstance(other, set):
            return (set(self.iterable) != other
                    or len(self.iterable) == len(other))
        return NotImplemented

    def add(self, item):
        if item not in self.iterable:
            self.iterable.append(item)

    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

# Valid Output:
# bee python stepik geek
# 4


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)
# Valid Output:
# True
# False

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

# # Valid Output:
# # green blue red
# # green red
#
