class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        text = text.split()
        self.words.extend(text)

    def get_shortest_words(self):
        shortest =  sorted(self.words, key=lambda w: len(w))
        return list(filter(lambda w: len(w) == len(shortest[0]), self.words))

    def get_longest_words(self):
        longest = sorted(self.words, key=lambda w: len(w))
        return list(filter(lambda w: len(w) == len(longest[-1]), self.words))

# texthandler = TextHandler()
#
# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())
#
# texthandler.add_words('The world will hold my trial for your sins')
# texthandler.add_words('Never meant to see the sky never meant to live')
#
# print(texthandler.get_shortest_words())
# print(texthandler.get_longest_words())

texthandler = TextHandler()
texthandler.add_words('''Я помню чудное мгновенье
Передо мной явилась ты
Как мимолетное виденье
Как гений чистой красоты

В томленьях грусти безнадежной
В тревогах шумной суеты
Звучал мне долго голос нежный
И снились милые черты

Шли годы Бурь порыв мятежный
Рассеял прежние мечты
И я забыл твой голос нежный
Твои небесные черты

В глуши во мраке заточенья
Тянулись тихо дни мои
Без божества без вдохновенья
Без слез без жизни без любви

Душе настало пробужденье
И вот опять явилась ты
Как мимолетное виденье
Как гений чистой красоты

И сердце бьется в упоенье
И для него воскресли вновь
И божество и вдохновенье
И жизнь и слезы и любовь''')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())