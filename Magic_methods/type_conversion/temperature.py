class Temperature:
    @classmethod
    def from_fahrenheit(cls, temp_fahr):
        celsius = (temp_fahr - 32) * (5 / 9)
        return Temperature(celsius)

    def __init__(self, temperature):
        self.temperature = temperature

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)

    def to_fahrenheit(self):
        fahrenheit = ((9 / 5) * self.temperature) + 32
        return fahrenheit

t = Temperature(5.5)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

t1 = Temperature(1)
t2 = Temperature(0)
t3 = Temperature(-1)

print(bool(t1))
print(bool(t2))
print(bool(t3))

t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())
