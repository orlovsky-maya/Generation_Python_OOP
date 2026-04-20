from random import shuffle


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}{self.rank}"

class Deck:
    _deck = [Card(s, r) for s in ("♣", "♢", "♡", "♠") for r in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")]

    def shuffle(self):
        if len(self._deck) == 52:
            shuffle(self._deck)
        else:
            raise ValueError("Перемешивать можно только полную колоду")

    def deal(self):
        if len(self._deck) != 0:
            return self._deck.pop()
        else:
            raise ValueError("Все карты разыграны")

    def __str__(self):
        return f"Карт в колоде: {len(self._deck)}"


# Входные данные 1
print(Card('♣', '4'))
print(Card('♡', 'A'))
print(Card('♢', '10'))

# Выходные данные 1
#
# ♣4
# ♡A
# ♢10

# Входные данные2
deck = Deck()

print(deck)
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(type(deck.deal()))
print(deck)
# Выходные данные 2
# Карт в колоде: 52
# ♠A
# ♠K
# ♠Q
# <class '__main__.Card'>
# Карт в колоде: 48

# Входные данные3
deck = Deck()

for _ in range(52):
    deck.deal()

try:
    deck.deal()
except ValueError as error:
    print(error)

# Выходные данные3
# Все карты разыграны

# Входные данные4
deck = Deck()

deck.deal()

try:
    deck.shuffle()
except ValueError as error:
    print(error)

# Выходные данные4

# Перемешивать можно только полную колоду