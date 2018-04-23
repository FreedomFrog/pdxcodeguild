from card import Card
from random import shuffle

class Deck:
    SUITS = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    RANKS = {'Ace':1 , 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
             'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'King':10, 'Queen':10, 'King':10}


    def __init__(self, number_decks=1):
        self.hopper = []
        self.number_decks = number_decks
        self.shuffle()
        self.hopper = self.generate_deck()

    def generate_deck(self):
        decks = []
        for i in range(self.number_decks):
            for s in self.SUITS:
                for r, v in self.RANKS.items():
                    decks.append(Card(s, r, v))
        return decks


    def shuffle(self):
        shuffle(self.hopper)

if __name__ == '__main__':
    deck = Deck()
    print(deck.hopper)
