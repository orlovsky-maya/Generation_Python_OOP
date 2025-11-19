# It will be solved after course for professional
from contextlib import contextmanager

@contextmanager
def safe_write(filename):
    try:
        filename_copy = filename
        file = open(filename_copy, mode='w')
        yield file
    except Exception as error:
        print(f"Во время записи в файл было возбуждено исключение {type(error).__name__}")


# with safe_write('undertale.txt') as file:
#     file.write('Тень от руин нависает над вами, наполняя вас решительностью')
#
# with open('undertale.txt') as file:
#     print(file.read())

# Valid output
# Тень от руин нависает над вами, наполняя вас решительностью

with safe_write('under_tale.txt') as file:
    file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')

with safe_write('under_tale.txt') as file:
    print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file, flush=True)
    raise ValueError

with open('under_tale.txt') as file:
    print(file.read())

# Valid output
# Во время записи в файл было возбуждено исключение ValueError
# Тень от руин нависает над вами, наполняя вас решительностью
