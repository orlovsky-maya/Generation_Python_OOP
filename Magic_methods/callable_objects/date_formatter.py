from datetime import date

class DateFormatter:
    dates = {"ru": '%d.%m.%Y',
             "us": '%m-%d-%Y',
             "ca": '%Y-%m-%d',
             "br": '%d/%m/%Y',
             "fr": '%d.%m.%Y',
             "pt": '%d-%m-%Y'}

    def __init__(self, country_code):
        self.country_code = country_code

    def __call__(self, d: date):
        return d.strftime(DateFormatter.dates[self.country_code])

ru_format = DateFormatter('ru')

print(ru_format(date(2022, 11, 7)))

us_format = DateFormatter('us')

print(us_format(date(2022, 11, 7)))

ca_format = DateFormatter('ca')

print(ca_format(date(2022, 11, 7)))