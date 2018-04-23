import hand

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hands = []

    def get_bet(self):
        a_bet = self.bet_on_hand()
        return a_bet

    def make_hand(self, a_card):
        if self.name == 'Dealer':
            a_bet = 0
        else:
            a_bet = self.get_bet()
        self.hands.append(hand.Hand(a_bet, a_card))

    def bet_on_hand(self):
        usr_in = float(input("{}, how much would you like to bet? $".format(self.name)))
        while True:
            if usr_in - self.money < 0:
                self.money -= usr_in
                break
            else:
                print(f'You have ${self.money}')
                usr_in = float(input("How much would you like to bet? $"))
        return usr_in


    def clear_hands(self):
        self.hands = []

    def check_split_hand(self):
        result = False
        if self.hands[0].check_if_split() and self.hands[0].bet < self.money:
            result = True
        return result

    def split_hand(self):
        self.make_hand()
        self.hands[1].get_card(self.hand[0].split_card)


    def win_money(self, amt):
        self.money += amt



