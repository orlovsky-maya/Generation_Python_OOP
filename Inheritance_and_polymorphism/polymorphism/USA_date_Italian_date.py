from abc import abstractmethod, ABC
from datetime import datetime, date

class DataFormat(ABC):
    ISO_FORMAT = "%Y-%m-%d"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.d = date(self.year, self.month, self.day)

    @abstractmethod
    def format(self):
       pass

    def iso_format(self):
        d = date(self.year, self.month, self.day)
        return datetime.strftime(d, self.ISO_FORMAT)

class USADate(DataFormat):
    DATE_FORMAT = "%m-%d-%Y"

    def format(self):
        return datetime.strftime(self.d, self.DATE_FORMAT)

class ItalianDate(DataFormat):
    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self, year, month, day):
        super().__init__(year, month, day)

    def format(self):
        return datetime.strftime(self.d, self.DATE_FORMAT)




# Sample Input 1:

usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())

# Sample Output 1:
#
# 04-06-2023
# 2023-04-06

# Sample Input 2:

italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())

# Sample Output 2:
#
# 06/04/2023
# 2023-04-06

