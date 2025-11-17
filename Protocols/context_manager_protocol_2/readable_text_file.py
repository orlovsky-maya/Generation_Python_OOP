class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, mode='r', encoding='utf-8')
        return self.file.read().splitlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile('glados_quotes.txt') as file:
    for line in file:
        print(line)

# Valid output
# Только посмотрите!
# Как величаво она парит в воздухе
# Как орел
# На воздушном шаре


with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)


# Valid output
# Я кашлянул в звенящей тишине,
# И от шального эха стало жутко…
# Расскажет ли утятам обо мне
# под утро мной испуганная утка?