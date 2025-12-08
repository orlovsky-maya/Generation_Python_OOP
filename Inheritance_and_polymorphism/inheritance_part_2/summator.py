class Summator:
    def __init__(self, degree=1):
        self.degree = degree

    def total(self, n):
        summa = 0
        for i in range(1, n + 1):
            summa += i **  self.degree
        return summa

class SquareSummator(Summator):
    def __init__(self):
        super().__init__(degree=2)

class QubeSummator(Summator):
    def __init__(self):
        super().__init__(degree=3)

class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(degree=m)

print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))
# Valid output
# True
# True

summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27

# Valid output
# 6
# 14
# 36

summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27

# Valid output

# 6
# 14
# 36