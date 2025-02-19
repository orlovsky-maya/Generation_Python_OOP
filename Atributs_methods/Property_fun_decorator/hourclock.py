class HourClock:
    def __init__(self, hours: int):
        self.hours = hours


    def get_hours(self):
        return self._hours

    def set_hours(self, new_hours):
        if isinstance(new_hours, int) and new_hours in range(1, 13):
            self._hours = new_hours
        else:
            raise ValueError ('Некорректное время')

    hours = property(get_hours, set_hours)

try:
    HourClock('pizza time 🕷')
except ValueError as e:
    print(e)


time = HourClock(7)

print(time.hours)
time.hours = 9
print(time.hours)