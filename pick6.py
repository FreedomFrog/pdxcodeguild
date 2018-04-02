import random

def pick_six():
    lst_six = random.sample(range(1, 100), 6)
    return lst_six


def is_match(master_lst, usr_lst):
    num_matches = 0
    for index, value in enumerate(usr_lst):
        if master_lst[index] == value:
            num_matches += 1
    return num_matches


def winnings(number_matches):
    dollars = -2
    if number_matches == 1:
        dollars += 4
    elif number_matches == 2:
        dollars += 7
    elif number_matches == 3:
        dollars += 100
    elif number_matches == 4:
        dollars += 50000
    elif number_matches == 5:
        dollars += 1000000
    elif number_matches == 6:
        dollars += 25000000
    return dollars

def manual_play():
    lst_numbers = []
    while len(lst_numbers) < 6:
        usr_num = input('Choose a number between 1 and 99: ')
        lst_numbers.append(usr_num)
    print('You are playing ' + str(lst_numbers) + ' good luck...')
    return lst_numbers

def bailed_out():
    result = False
    usr_in = input('Would you like a bailout? (y/n): ')
    if usr_in == 'y':
        result = True
    return result

def return_on_investment(cur_bal, cur_play):
    roi = 1+(cur_bal - (cur_play * 2)) / (cur_play * 2)
    return roi

def big_play():
    win_tick = pick_six()
    play_count = 0
    balance = 0
    while play_count < 100000:
        my_tick = pick_six()
        match = is_match(win_tick, my_tick)
        balance += winnings(match)
        play_count += 1
        roi = return_on_investment(balance, play_count)
        if winnings(match) > 5:
            print('You won ${}, phew that was lucky'.format(winnings(match)))
            print('The winning ticket was ' + str(win_tick))
            print('Your ticket was ' + str(my_tick))

    print('Your balance is {}'.format(balance))
    print('Your ROI is {}'.format(roi))

def small_play():
    balance = 0
    play_count = 0
    while balance <= 0:
        master = pick_six()
        usr_lst = manual_play()
        matched = is_match(master, usr_lst)
        balance += winnings(matched)
        play_count += 1
        roi = return_on_investment(balance, play_count)
        print('Your current balance is {}'.format(balance))
        print('Your ROI is {}'.format(roi))
        print('The winning ticket was ' + str(master))
        if winnings(matched) > 0:
            print('You won ${}, phew that was lucky'.format(winnings(matched)))
        if balance < -10:
            bail = bailed_out()
            if bail:
                balance = 0
                print('Your current balance is now {}'.format(balance))

def play_to_win():
    win_tick = pick_six()
    balance = 0
    play_count = 0
    win = 0
    while win < 20000000:
        my_tick = pick_six()
        match = is_match(win_tick, my_tick)
        balance += winnings(match)
        win = winnings(match)
        play_count += 1
        roi = return_on_investment(balance, play_count)
        if winnings(match) > 200:
            print('You won ${}, phew that was lucky'.format(winnings(match)))
            print('The winning ticket was ' + str(win_tick))
            print('Your ticket was ' + str(my_tick))

    print('Your balance is {}'.format(balance))
    print('Your ROI is {}'.format(roi))
    print('This was on turn {}'.format(play_count))


def menu():
    select = ''
    while select != 's' and select != 'a' and select != 'p':
        select = input('Play (S)imple game, (A)dvanced game or (P)lay to win: ' ).lower()
    return select


def main():
    selection = menu()
    if selection == 's':
        small_play()
    if selection == 'a':
        big_play()
    if selection == 'p':
        play_to_win()


if __name__ == '__main__':
    main()