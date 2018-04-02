import hand

class Player:

    def __init__(self, dealer=False):
        self.player_num = 0
        self.name = ''
        self.money = 0
        self.bet = 0
        self.hand_of_cards = hand.Hand()
        self.start_name(dealer)
        self.start_money(dealer)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def start_name(self, dealer=False):
        if not dealer:
            has_name = input('What is the player\'s name?: ')
        elif dealer:
            has_name = 'Dealer'
        self.name = has_name

    def start_money(self, dealer=False):
        if not dealer:
            has_money = input('How much money does {} have?: $'.format(self.name))
        elif dealer:
            has_money = 99999999999
        self.money = float(has_money)

    def add_money(self, a_float):
        self.money += a_float

    def bet_amount(self, a_float):
        while a_float > self.money:
            a_float = float(input('You cannot enter an amount great than {}. How much would you like to bet?: $'.format(self.money)))
        self.money -= a_float
        self.bet = a_float

    def player_order(self, an_int):
        self.player_num = an_int

