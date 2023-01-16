import abc
import random
from tkinter import ttk


class AbstractPlayer(abc.ABC):
    def __init__(self, position):
        self.cards = []
        self.bet = 0
        self.position = position
        self.full_points = 0

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])

    def ask_card(self, deck, card_count):
        for _ in range(card_count):
            card = deck.get_card()
            self.cards.append(card)
        self.change_points()
        return True

    def card_print_player(self):
        for card in self.cards:
            print(card.suit, card.rank)


class Player(AbstractPlayer):
    def point_print_player(self):
        label3 = ttk.Label(text=f'Очки: {self.full_points}')
        label3.place(x=900, y=600)

    def refresh(self):
        ttk.Label(text=f'Очки: {self.full_points}').place(x=900, y=600)

    def change_bet(self, player_bet):
        self.bet = player_bet


class Bot(AbstractPlayer):
    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
