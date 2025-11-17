class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close and not self.closed():
            self.close()

    def write(self, text):
        if self.file1.closed or self.file2.closed or not self.writable():
            raise ValueError("Файл закрыт или недоступен для записи")
        else:
            self.file1.write(text)
            self.file2.write(text)


    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        elif self.file1.writable() and self.file2.writable():
            return True
        else:
            return False

    def closed(self):
        if self.file1.closed and self.file2.closed:
            return True
        else:
            return False

f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())


# Valid output
# True True
# You shall seal the blinding light that plagues their dreams
# You are the Vessel
# You are the Hollow Knight
# You shall seal the blinding light that plagues their dreams
# You are the Vessel
# You are the Hollow Knight


f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

f1 = open('file1.txt')
f2 = open('file2.txt')

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# Valid output
# True
# False

f1 = open('file1.txt', mode='r')
f2 = open('file2.txt', mode='w')

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# Valid output
# Файл закрыт или недоступен для записи

f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

try:
    with WriteSpy(f1, f2, to_close=True) as combined:
        combined.write('No cost too great')
except ValueError as error:
    print(error)

# Valid output
# Файл закрыт или недоступен для записи

f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')
f1.close()

with WriteSpy(f1, f2, to_close=True) as combined:
    print(combined.writable())

# Valid output
# False

f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2) as combined:
    pass

print(combined.closed())

# Valid output
# False