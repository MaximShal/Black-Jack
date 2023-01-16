from const import SUITS, RANKS
from itertools import product
from random import shuffle


class Card:
    def __init__(self, suit, rank, points):
        self.suit = suit
        self.rank = rank
        self.points = points
        # добавить картинку карт
        picture = None

    def __str__(self):
        massage = f'{self.rank} {self.suit} points: {str(self.points)}'
        return massage


class Deck:
    def __init__(self):
        self.cards = self._create_deck()
        shuffle(self.cards)

    @staticmethod
    def _create_deck():
        cards = []
        for suit, rank in product(SUITS, RANKS):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10
            c = Card(suit=suit, rank=rank, points=points)
            cards.append(c)
        return cards

    def get_card(self):
        return self.cards.pop()
