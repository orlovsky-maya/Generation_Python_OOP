from datetime import date


class WeatherWarning:
    def rain(self):
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print("Ожидается снег и усиление ветра")

    def low_temperature(self):
        print("Ожидается сильное понижение температуры")

class WeatherWarningWithDate(WeatherWarning):

    def rain(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().rain()

    def snow(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().snow()

    def low_temperature(self, d: date):
        print(d.strftime('%d.%m.%Y'))
        super().low_temperature()


print(issubclass(WeatherWarningWithDate, WeatherWarning))

# Valid output
# True

weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()
# Valid output
# True
# Ожидаются сильные дожди и ливни с грозой
# Ожидается снег и усиление ветра
# Ожидается сильное понижение температуры

weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)

weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)

# Valid output

# 12.12.2022
# Ожидаются сильные дожди и ливни с грозой
# 12.12.2022
# Ожидается снег и усиление ветра
# 12.12.2022
# Ожидается сильное понижение температуры