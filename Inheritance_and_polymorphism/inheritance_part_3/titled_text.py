class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.content = content
        return instance

    def __init__(self,  content, text_title):
        self.content = content
        self.text_title = text_title

    def title(self):
        return self.text_title

titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))

# Valid output
# Сreate a class Soda
# Homework
# True


titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)


# Valid output
# True