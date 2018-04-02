import card
import random


ranks = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"]


suits = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Deck:
    def __init__(self, an_int=1):
        self.contents = []
        self.num_decks = an_int
        self.make_cards_in_decks(self.num_decks)
        self.shuffle_cards()

    def __repr__(self):
        return str(self.contents)

    def make_cards_in_decks(self, an_int):
        for i in range(an_int):
            self.contents.extend([card.Card(rank, suit) for rank in ranks for suit in suits])

    def shuffle_cards(self):
        random.shuffle(self.contents)

    def deal_card(self):
        return self.contents.pop(0)

#
# d1 = Deck()
# print(d1)
# print(d1.shuffle_cards())
# print(d1)