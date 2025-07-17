from functools import total_ordering

@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month


    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        elif isinstance(other, tuple) and len(other) == 2:
            year, month = other
            return self.year == year and self.month == month
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Month):
            return (self.year, self.month) < (other.year, other.month)
        elif isinstance(other, tuple) and len(other) == 2:
            return (self.year, self.month) < other
        return NotImplemented

print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(sorted(months))

months = [Month(1998, 12), Month(2000, 1), Month(1999, 12)]

print(min(months))
print(max(months))