from collections.abc import Sequence
class DNA(Sequence):
    complim_dict = {
        "T": "A",
        "A": "T",
        "G": "C",
        "C": "G"
    }
    def __init__(self, chain):
        self.chain = chain
        self.chain_2 = [self.complim_dict.get(key) for key in self.chain]

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Индекс должен быть целым числом')
        if key >= len(self.chain):
            raise IndexError('Неверный индекс')
        return self.chain[key], self.chain_2[key]

    def __len__(self):
        return len(self.chain)

    def __eq__(self, other):
        if isinstance(other, DNA):
            return self.chain == other.chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, DNA):
            return DNA(self.chain + other.chain)
        return NotImplemented

    def __contains__(self, other):
        return other in self.chain

    def __str__(self):
        return f"{self.chain}"




# Sample Input 1:

dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])

# Sample Output 1:
#
# ('A', 'T')
# ('G', 'C')
# ('T', 'A')
# ('C', 'G')
# ('C', 'G')
# ('T', 'A')

# Sample Input 2:

dna = DNA('AGT')

print(dna)
print(len(dna))
print('A' in dna)
print('C' in dna)

# Sample Output 2:
#
# AGT
# 3
# True
# False

# Sample Input 3:

dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = dna1 + dna2
dna4 = dna2 + dna1

print(dna3, type(dna3))
print(dna4, type(dna4))

# Sample Output 3:
#
# ACGTTTAAT <class '__main__.DNA'>
# TTTAATACG <class '__main__.DNA'>
#
# Sample Input 4:

dna1 = DNA('ACG')
dna2 = DNA('TTTAAT')
dna3 = DNA('TTTAAT')

print(dna1 == dna2)
print(dna2 == dna3)
print(dna1 != dna3)
print(dna2 != dna3)

# Sample Output 4:
#
# False
# True
# True
# False


# TEST_5:
dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

print(*dna)
print(*reversed(dna))
print('A' in dna)
print('C' not in dna)

# TEST_5:
# ('T', 'A') ('G', 'C') ('A', 'T') ('A', 'T') ('C', 'G') ('C', 'G') ('T', 'A') ('G', 'C') ('A', 'T') ('C', 'G') ('C', 'G') ('T', 'A') ('C', 'G') ('G', 'C') ('A', 'T') ('T', 'A') ('T', 'A') ('T', 'A') ('C', 'G') ('A', 'T') ('A', 'T') ('G', 'C') ('G', 'C') ('G', 'C')
# ('G', 'C') ('G', 'C') ('G', 'C') ('A', 'T') ('A', 'T') ('C', 'G') ('T', 'A') ('T', 'A') ('T', 'A') ('A', 'T') ('G', 'C') ('C', 'G') ('T', 'A') ('C', 'G') ('C', 'G') ('A', 'T') ('G', 'C') ('T', 'A') ('C', 'G') ('C', 'G') ('A', 'T') ('A', 'T') ('G', 'C') ('T', 'A')
# True
# False
