import card

class Hand:
    def __init__(self, bet, card_obj):
        self.holding_cards = [card_obj]
        self.hand_value = 0
        self.bet = bet
        self.active = True
        self.split = False

    def get_card(self, card_obj):
        self.holding_cards.append(card_obj)
        self.update_hand_value()
        self.check_if_split()
        if self.check_bust():
            self.active = False
            self.clear_bet()

    def update_hand_value(self):
        self.hand_value = 0
        for card_obj in self.holding_cards:
            self.hand_value += card_obj.value

    def check_if_split(self):
        self.split = False
        if len(self.holding_cards) == 2:
            if self.holding_cards[0].rank == self.holding_cards[1].rank:
                self.split = True

    def split_card(self):
        return self.holding_cards.pop()

    def double_bet(self):
        self.bet += self.bet

    def clear_bet(self):
        self.bet = 0

    def check_bust(self):
        bust = False
        if self.hand_value > 21:
            bust = True
        return bust


