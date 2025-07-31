def time(hours, minutes):
    if minutes >= 60:
        extra_hour = minutes // 60
        hours += extra_hour
        minutes = minutes % 60
    if hours >= 24:
        hours = hours % 24
    return hours, minutes


class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = time(hours, minutes)
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def __add__(self, other):
        if isinstance(other, Time):
            hours = self.hours + other.hours
            minutes = self.minutes + other.minutes
            return Time(hours, minutes)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other.hours
            self.minutes += other.minutes
            self.hours, self.minutes = time(self.hours , self.minutes)
            return self
        else:
            return NotImplemented

time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

t = Time(22, 0)
t += Time(3, 0)
print(t)
