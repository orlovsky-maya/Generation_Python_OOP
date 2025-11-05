class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, item):
        return self.sequence[::-1][item]

    def __len__(self):
        return len(self.sequence)


reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])

# Valid Output:
# 5
# 4
# 3

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])

# Valid Output:
# 5
# 6

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))

# Valid Output:
# 5
# 7