import deck
import card


class Hand:
    def __init__(self):

        self.play_cards = []
        self.hand_value = 0

    def get_card(self, a_card):
        self.play_cards.append(a_card)
        self.sum_play_cards()

    def sum_play_cards(self):
        total = 0
        for a_card in self.play_cards:
            total += a_card.bk_value
        self.hand_value = total

    def __repr__(self):
        return str(self.play_cards) + str(self.hand_value)

