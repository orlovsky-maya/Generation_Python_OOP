class Wordplay:
    def __init__(self, words=None):
        if words is None:
            words = []
        self.words = words.copy()

    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, length):
        return list(filter(lambda word: len(word) == length, self.words))

    def only(self, *args):
        results_words = []
        for w in self.words:
            if set(w).issubset(args):
                results_words.append(w)
        return results_words

    def avoid(self, *args):
        results_words = []
        for w in self.words:
            if set(w).isdisjoint(args):
                results_words.append(w)
        return results_words


wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))