from Deck import Deck
import Player
from tkinter import ttk
import time


class Game:
    def __init__(self):
        self.players_bot = []
        self.player = None
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    # /// обрання ставки ботами
    def ask_bet_bot(self):
        for player in self.players_bot:
            player.change_bet(self.max_bet, self.min_bet)
            print(player, f' зробив ставку {player.bet}')

    # /// видача карт по дві ботам
    def first_delivery(self):
        for player in self.players_bot:
            player.ask_card(self.deck, 2)

    def take_card(self, player):
        player.ask_card(self.deck, 1)

    def player_card_button(self):
        self.player.ask_card(self.deck, 1)
        if self.player.full_points > 21:
            pass
        self.player.refresh()
        print(self.player.cards[-1])

    def start_game(self, bots_count):
        # /// створення ботів певної кількості
        for i in range(bots_count):
            b = Player.Bot(position=i)
            self.players_bot.append(b)
            print(b, ' is created!')

        self.ask_bet_bot()
        self.first_delivery()

        # /// створення гравця
        self.player = Player.Player(position=3)

        def change_player_bet():
            def make_bet():
                try:
                    value = int(entry1.get())
                    if value < self.max_bet and value > self.min_bet:
                        self.player.change_bet(value)
                        entry1.destroy(), btn1.destroy(), label1.destroy()
                        label2 = ttk.Label(text=f'Ставка {self.player.bet}')
                        label2.place(x=1000, y=600)
                        self.player.ask_card(self.deck, 2)
                        self.player.point_print_player()
                        self.player.card_print_player()

                        ttk.Button(width=40, text='Додаткова\nкарта', command=self.player_card_button).place(x=50, y=400)
                except ValueError:
                    pass
            entry1 = ttk.Entry()
            entry1.place(x=900, y=600)
            label1 = ttk.Label(text='Зроби ставку від 0 до 20')
            label1.place(x=900, y=570)
            btn1 = ttk.Button(text="Підтвердити", command=make_bet)
            btn1.place(x=1030, y=600)
            time.sleep(5)


        print('it works')
        change_player_bet()
        print('it works 2')
