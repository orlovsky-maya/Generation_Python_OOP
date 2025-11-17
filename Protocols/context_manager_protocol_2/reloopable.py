class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return self.file.readlines()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with open('file.txt', 'w') as file:
    file.write('Evil is evil\n')
    file.write('Lesser, greater, middling\n')
    file.write('Makes no difference\n')

with Reloopable(open('file.txt')) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())

#Valid output
# Evil is evil
# Lesser, greater, middling
# Makes no difference
# Evil is evil
# Lesser, greater, middling
# Makes no difference