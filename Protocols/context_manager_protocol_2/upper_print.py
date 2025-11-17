import sys

class UpperPrint:
    def __enter__(self):
        self.standard_output = sys.stdout.write
        sys.stdout.write = lambda text: self.standard_output(text.upper())


    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.standard_output

print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')


# # Valid Output
# Если жизнь одаривает вас лимонами — не делайте лимонад
# Заставьте жизнь забрать их обратно!
# МНЕ НЕ НУЖНЫ ТВОИ ПРОКЛЯТЫЕ ЛИМОНЫ!
# ЧТО МНЕ С НИМИ ДЕЛАТЬ?
# Требуйте встречи с менеджером, отвечающим за жизнь!

with UpperPrint():
    print('Bee', 'Geek', 'Love', sep=' one ', end=' end')

# Valid Output
# BEE ONE GEEK ONE LOVE END
