import sys
from contextlib import contextmanager

@contextmanager
def reversed_print():
    standart_output = sys.stdout.write
    sys.stdout.write = lambda x: standart_output(x[::-1])
    yield
    sys.stdout.write = standart_output

print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')

# # Valid output
# Вывод вне блока with
# htiw аколб иртунв довыВ
# Вывод вне блока with

