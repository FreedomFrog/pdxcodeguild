import card
import deck
import hand
import player

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