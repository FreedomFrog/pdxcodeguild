import player
import deck

class Blackjack:
    def __init__(self):
        self.players = self.get_players()
        self.dealer = self.make_dealer()
        self.deck = self.get_num_decks()
        self.make_initial_hands()


    def get_players(self):
        players = []
        num_players = int(input('How many players? '))
        for i in range(num_players):
            player_name = input('What is player {}s name? '.format(i+1))
            player_money = float(input('How much money does {} have? $'.format(player_name)))
            players.append(player.Player(player_name,player_money))
        return players

    def print_all_players(self):
        for player_obj in self.players:
            print('Player {} has ${}'.format(player_obj.name, player_obj.money))
            print('{} has {}'.format(player_obj.name, player_obj.hands.hand[:]))


    def make_dealer(self):
        return player.Player('Dealer', 999999999)


    def get_num_decks(self):
        num_decks = int(input('How many decks will be played? '))
        return deck.Deck(num_decks)

    def place_bets(self):
        for player_obj in self.players:
            player_obj.make_hand(self.deck.hopper.pop())
        self.dealer.make_hand(self.deck.hopper.pop())

    def deal_initial_cards(self):
        to_deal = 1
        print(self.players)
        print(self.dealer)
        participants = self.players + [self.dealer]
        print(participants)
        while to_deal > 0:
            for player_obj in participants:
                print(player_obj.name)
                print(player_obj.hands[0].holding_cards)
                player_obj.hands[0].get_card(self.deck.hopper.pop())
                print(player_obj.hands[0].holding_cards)
            to_deal -= 1

    

    def make_initial_hands(self):
        self.place_bets()
        self.deal_initial_cards()





if __name__ == '__main__':
    game1 = Blackjack()
