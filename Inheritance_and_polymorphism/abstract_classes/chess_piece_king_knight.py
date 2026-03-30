from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, a, b):
        pass


class King(ChessPiece):
    def can_move(self, horizontal_2, vertical_2):
        horizontals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        if self.horizontal == horizontal_2 and self.vertical == vertical_2:
            return False
        if (abs(self.vertical - vertical_2) <= 1) and (
                abs(horizontals[self.horizontal] - horizontals[horizontal_2]) <= 1):
            return True
        else:
            return False


class Knight(ChessPiece):
    def can_move(self, horizontal_2, vertical_2):
        horizontals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        if self.horizontal == horizontal_2 and self.vertical == vertical_2:
            return False

        if (self.vertical - vertical_2) * (horizontals[self.horizontal] - horizontals[horizontal_2]) == 2 or (
                self.vertical - vertical_2) * (horizontals[self.horizontal] - horizontals[horizontal_2]) == -2:
            return True
        else:
            return False


# Sample Input:

# king = King('b', 2)
#
# print(king.can_move('c', 3))
# print(king.can_move('a', 1))
# print(king.can_move('f', 7))

# Sample Output:
#
# True
# True
# False


# TEST_2:
# knight = Knight('c', 3)
#
# print(knight.can_move('e', 5))
# print(knight.can_move('e', 4))

# TEST_2:
# False
# True

# TEST_3:
king = King('e', 3)

print(king.can_move('e', 3))
print(king.can_move('e', 4))
print(king.can_move('b', 1))

# TEST_3:
# False
# True
# False


# TEST_7:
kings = [King(h, v) for h in 'abcdefgh' for v in range(1, 9)]

for king in kings:
    print('*' * 20)
    for horizontal in 'abcdefgh':
        for vertical in range(1, 9):
            if king.can_move(horizontal, vertical):
                print(f'King({king.horizontal}{king.vertical})', f'{horizontal}{vertical}',
                      king.can_move(horizontal, vertical))

