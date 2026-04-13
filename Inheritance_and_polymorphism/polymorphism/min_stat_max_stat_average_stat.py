from abc import ABC, abstractmethod


class Stat(ABC):
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    @abstractmethod
    def result(self):
        pass

    def clear(self):
        self.iterable.clear()


class MinStat(Stat):
    def result(self):
        if len(self.iterable) == 0:
            return None
        else:
            return min(self.iterable)

class MaxStat(Stat):
    def result(self):
        if len(self.iterable) == 0:
            return None
        else:
            return max(self.iterable)

class AverageStat(Stat):
    def result(self):
        if len(self.iterable) == 0:
            return None
        else:
            return sum(self.iterable) / len(self.iterable)



# Sample Input 1:

minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
#
# Sample Output 1:
#
# 1
# 5
# 3.0

# Sample Input 2:

minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
#
# Sample Output 2:
#
# 1
# 5
# 3.0
#
# Sample Input 3:

minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())

# Sample Output 3:
#
# None
# None
# None
#
