import card
import deck
import hand
import player
import advise


def get_number_of_decks():
    num_decks = int(input('How many decks will we play?: '))
    deck_obj = deck.Deck(num_decks)
    return deck_obj


def get_number_of_players():
    str_input = input('How many players will play?: ')
    return int(str_input)


def get_bet(player_obj):
    if not player_obj.name == 'Dealer':
        a_bet = float(input("{} how much would you like to bet? $".format(player_obj.name)))
        player_obj.bet_amount(a_bet)
    return True


def win_blackjack(player_obj):
    win_amount = player_obj.bet * 1.5 + player_obj.bet
    player_obj.bet = 0
    player_obj.money += win_amount
    return True


def win_normal(player_obj):
    win_amount = player_obj.bet + player_obj.bet
    player_obj.bet = 0
    player_obj.money += win_amount
    return True


def dealer_lose(lst_of_players):
    for player_obj in lst_of_players:
        win_normal(player_obj)
    return True


def lose(player_obj):
    player_obj.bet = 0
    return True


def create_dealer():
    a_dealer = player.Player(dealer=True)
    return a_dealer


def create_players():
    lst_of_players = []
    num_players = get_number_of_players()
    for i in range(num_players):
        new_player = player.Player()
        new_player.player_num = i
        lst_of_players.append(new_player)
    lst_of_players.append(create_dealer())
    assign_player_number(lst_of_players)

    return lst_of_players


def remove_player(lst_of_players, index):
    del lst_of_players[index]
    return lst_of_players


def deal_all_bets(lst_of_players):
    for i in lst_of_players:
        get_bet(i)
    return True


def deal_single_card(player_obj, deck_obj):
    player_obj.hand_of_cards.get_card(deck_obj.deal_card())
    return True


def assign_player_number(lst_of_players):
    for index, value in enumerate(lst_of_players):
        value.player_order(index)
    return True


def deal_first_two_cards(lst_of_players, deck_obj):
    count = 0
    while count < 2:
        for a_player in lst_of_players:
            a_player.hand_of_cards.get_card(deck_obj.deal_card())
        count += 1
    return True


def reveal_player_cards(player_obj):
    if player_obj.name == 'Dealer':
        reveal = str(player_obj.hand_of_cards.play_cards[0])
    else:
        reveal = str(player_obj.hand_of_cards)
    return reveal


def has_bust(player_obj):
    result = False
    if player_obj.hand_of_cards.hand_value > 21:
        result = True
    return result


def has_split(player_obj):
    result = False
    player_cards = player_obj.hand_of_cards.play_cards
    if len(player_cards) == 2:
        if len(player_cards) != len(set(player_cards)):
            result = True
    return result


def has_blackjack(player_obj):
    result = False
    player_cards = player_obj.hand_of_cards.play_cards
    if len(player_cards) == 2 and player_obj.hand_of_cards.hand_value == 11:
        if player_cards[0].bk_value == 1 or player_cards[1].bk_value == 1:
            result = True
    return result


def check_blackjack(player_obj):
    result = False
    if has_blackjack(player_obj):
        print('BLACKJACK!')
        win_blackjack(player_obj)
        result = True
    return result

def check_dealer_blackjack(player_obj):
    result = False
    if has_blackjack(player_obj):
        print('Dealer blackjack')
        result = True
    return result


def get_player_choice(player_obj):
    poss_split = has_split(player_obj)
    player_choice = ''
    if poss_split:
        print('(S)tand, (H)it, (D)ouble, (SP)lit')
        poss_choice = ['S', 'H', 'D', 'SP']
    else:
        print('(S)tand, (H)it, (D)ouble')
        poss_choice = ['S', 'H', 'D']
    while player_choice not in poss_choice:
        player_choice = input('{}, what would you like to do: '.format(player_obj.name)).capitalize()
    return player_choice


def play_players(lst_of_players, curr_deck):
    dealer_card = reveal_player_cards(lst_of_players[-1])
    for player_obj in lst_of_players[:-1]:
        player_hand = reveal_player_cards(player_obj)
        check_blackjack(player_obj)
        advise_str = advise.advise(player_obj, lst_of_players[-1])
        #make better
        print(player_hand + dealer_card + advise_str)
        while True:
            play_choice = get_player_choice(player_obj)
            if play_choice == 'S':
                break
            if play_choice == 'H':
                deal_single_card(player_obj, curr_deck)
                print(reveal_player_cards(player_obj))
                bust = has_bust(player_obj)
                if bust:
                    lose(player_obj)
                    play_choice = 'SU'
                    break
            if play_choice == 'D':
                player_obj.money -= player_obj.bet
                player_obj.bet += player_obj.bet
                deal_single_card(player_obj, curr_deck)
                print(reveal_player_cards(player_obj))
                bust = has_bust(player_obj)
                if bust:
                    lose(player_obj)
                    play_choice = 'SU'
                    break
    return True

def play_dealer(lst_of_players, curr_deck):
    dealer_hand = reveal_player_cards(lst_of_players[-1])
    print(dealer_hand)
    dealer_obj = lst_of_players[-1]

    while dealer_obj.hand_of_cards.hand_value <= 16:
        deal_single_card(lst_of_players[-1], curr_deck)
        dealer_hand = lst_of_players[-1].hand_of_cards.play_cards
        print('dealer hits')
        print(dealer_hand)
        for a_card in dealer_obj.hand_of_cards.play_cards:
            if a_card.bk_value == 1 and dealer_obj.hand_of_cards.hand_value < 11:
                a_card.bk_value += 10
    if dealer_obj.hand_of_cards.hand_value > 22:
        for a_card in dealer_obj.hand_of_cards.play_cards:
            if a_card.bk_value == 11:
                a_card.bk_value = 1
                break
            else:
                dealer_lose(lst_of_players)
                print('dealer lost')
                break
    for player_obj in lst_of_players:
        if player_obj.hand_of_cards.hand_value == dealer_obj.hand_of_cards.hand_value:
            player_obj.money += player_obj.bet
            if player_obj.name == 'Dealer':
                pass
            else:
                print('dealer pushed with {}'.format(player_obj.name))
        elif player_obj.hand_of_cards.hand_value > dealer_obj.hand_of_cards.hand_value and player_obj.hand_of_cards.hand_value < 22:
            player_obj.money += player_obj.bet * 2
            print('dealer lost to {}'.format(player_obj.name))
        else:
            player_obj.bet = 0
    return True

def reset_hands(lst_of_players):
    for player_obj in lst_of_players:
        player_obj.hand_of_cards = hand.Hand()
    return True


def main():
    lst_parti = create_players()
    hopper = get_number_of_decks()
    while True:
        reset_hands(lst_parti)
        deal_all_bets(lst_parti)
        for index, player in enumerate(lst_parti):
            if player.bet == 0 and player.money == 0:
                remove_player(lst_parti, index)
                print('{} has been removed'.format(player.name))
        deal_first_two_cards(lst_parti, hopper)
        if check_dealer_blackjack(lst_parti[-1]):
            for player in lst_parti:
                if check_blackjack(player):
                    player.money += player.bet
                    lose(player)
                else:
                    lose(player)

            continue
        print('playing players')
        play_players(lst_parti, hopper)
        print('playing dealer')
        play_dealer(lst_parti, hopper)


if __name__ == '__main__':
    main()
