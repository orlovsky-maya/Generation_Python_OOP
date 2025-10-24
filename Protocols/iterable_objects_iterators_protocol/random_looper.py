from random import shuffle


class RandomLooper:
    def __init__(self, *args):
       self.data = [elem for arg in args for elem in arg]
       shuffle(self.data)
       self.index = -1
       self.length = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= self.length:
            raise StopIteration
        return self.data[self.index]

randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])
print(list(randomlooper))
print(list(randomlooper))

# Valid Output:
# ['green', 'red', 'blue', 'purple']
# []


colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))

# Valid Output:
# ['circle', 'red', 'purple', 'octagon', 'triangle', 'green', 'blue', 'square']