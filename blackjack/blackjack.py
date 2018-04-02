import card
import deck
import hand
import player


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
    player_obj.hand_of_cards.insert(deck_obj.deal_card())
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


def pairs(player_hand_value, dealer_hand_cards):
    dealer_shown_value = dealer_hand_cards[0].bk_value
    if player_hand_value == 2 or player_hand_value == 16:
        result = 'SP'
    if player_hand_value == 20:
        result = 'S'
    if player_hand_value == 18:
        result = 'SP'
        if dealer_shown_value == 7 or dealer_shown_value == 10 or dealer_shown_value == 1:
            result = 'S'
    if player_hand_value == 14:
        result = 'SP'
        if dealer_shown_value > 7:
            result = 'H'
    if player_hand_value == 10:
        result = 'Dh'
        if dealer_shown_value > 9:
            result = 'H'
    if player_hand_value == 8:
        result = 'H'
        if dealer_shown_value == 5 or dealer_shown_value == 6:
            result = 'SP'
    if player_hand_value == 4 or player_hand_value == 6:
        result = 'SP'
        if dealer_shown_value > 7:
            result = 'H'
    return result


def soft_totals(player_hand_value, dealer_hand_cards):
    dealer_shown_value = dealer_hand_cards[0].bk_value
    if player_hand_value > 8:
        result = 'S'
        if dealer_shown_value == 6:
            result = 'Ds'
    if player_hand_value == 8:
        result = 'Ds'
        if dealer_shown_value == 7 or dealer_shown_value == 8:
            result = 'S'
        if dealer_shown_value > 8:
            result = 'H'
    if player_hand_value == 7:
        result = 'H'
        if 2 < dealer_shown_value < 7:
            result = 'Dh'
    if player_hand_value == 5 or player_hand_value == 6:
        result = 'H'
        if 3 < dealer_shown_value < 7:
            result = 'Dh'
    if player_hand_value == 3 or player_hand_value == 4:
        result = 'H'
        if 4 < dealer_shown_value < 7:
            result = 'Dh'
    return result


def hard_totals(player_hand_value, dealer_hand_cards):
    dealer_shown_value = dealer_hand_cards[0].bk_value
    if player_hand_value > 16:
        result = 'S'
    elif player_hand_value > 12:
        result = 'S'
        if dealer_shown_value > 6:
            result = 'H'
    if player_hand_value == 12:
        result = 'H'
        if 3 < dealer_shown_value < 7:
            result = 'S'
    if player_hand_value == 11:
        result = 'Dh'
    if player_hand_value == 10:
        result = 'Dh'
        if dealer_shown_value > 9:
            result = 'H'
    if player_hand_value == 9:
        result = 'H'
        if 2 < dealer_shown_value < 7:
            result = 'Dh'
    if player_hand_value < 9:
        result = 'H'
    return result


def advise(player_obj, dealer_obj):
    for ind_card in player_obj.hand_of_cards.play_cards:
        if len(player_obj.hand_of_cards.play_cards) == 2 and player_obj.hand_of_cards.play_cards[0] == player_obj.hand_of_cards.play_cards[1]:
            result = pairs(player_obj.hand_of_cards.hand_value, dealer_obj.hand_of_cards.hand_of_cards)
        elif ind_card.bk_value == 1 and player_obj.hand_of_cards.hand_value < 11:
            result = soft_totals(player_obj.hand_of_cards.hand_value, dealer_obj.hand_of_cards.play_cards)
        else: # player_obj.hand_of_cards.hand_value > 11:
            result = hard_totals(player_obj.hand_of_cards.hand_value, dealer_obj.hand_of_cards.play_cards)
    return result





def has_split(player_obj):
    result = False
    player_cards = player_obj.hand_of_cards.play_cards
    if len(player_cards) == 2:
        if len(player_cards) != len(set(player_cards)):
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
        player_choice = input('{}, what would you like to do'.format(player_obj.name)).capitalize()
    return player_choice


def play_players(lst_of_players):
    dealer_card = reveal_player_cards(lst_of_players[-1])
    for player_obj in lst_of_players[:-1]:
        player_hand = reveal_player_cards(player_obj)
        advise_str = advise(player_obj, lst_of_players[-1])
        print(player_hand + dealer_card + advise_str)
        play_choice = get_player_choice(player_obj)
        print(play_choice)


def main():
    lst_parti = create_players()
    hopper = get_number_of_decks()
    deal_all_bets(lst_parti)
    deal_first_two_cards(lst_parti, hopper)
    play_players(lst_parti)


if __name__ == '__main__':
    main()
