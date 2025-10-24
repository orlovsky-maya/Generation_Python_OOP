class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        result = list(dict.fromkeys(args, 'junior').items())
        return self.junior.extend(result)

    def add_senior(self, *args):
        result = list(dict.fromkeys(args, 'senior').items())
        return self.senior.extend(result)

    def __iter__(self):
        developers = self.junior + self.senior
        yield from developers



beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')

# Valid Output:
# ('Timur', 'junior')
# ('Arthur', 'junior')
# ('Valery', 'junior')
# ('Gvido', 'senior')

beegeek = DevelopmentTeam()

print(len(list(beegeek)))

# Valid Output: 0

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')

# Valid Output:
# ('Timur', 'junior')
# ('Arthur', 'junior')
# ('Valery', 'junior')