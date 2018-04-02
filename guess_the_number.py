import random


def get_user_guess():
    while True:
        guess = input('guess the number: ')
        if guess.isdigit():
            break
    return guess


def towards_target(cor_num, usr_num, last_guess):
    guess_diff = abs(cor_num - usr_num)
    last_guess_diff = abs(cor_num - last_guess)

    if guess_diff >= last_guess_diff:
        towards = False
    else:
        towards = True

    return towards


def gen_response(cor_num, usr_num, last_guess, guess_count):
    win = False
    result = ''
    if cor_num == usr_num:
        result = 'Correct! You guessed {} times.'.format(guess_count)
        win = True

    else:
        if guess_count > 0:
            if towards_target(cor_num, usr_num, last_guess):
                result = 'Warmer...'
            else:
                result = 'Colder...'
        result += 'try again'
    return result, win


def game1():
    last_time = 0
    count = 0
    x = random.randint(1,10)
    active = True
    while active:

        guess = int(get_user_guess())
        response, win = gen_response(x, guess, last_time, count)
        print(response)
        count += 1
        last_time = guess
        if win == True:
            break


def am_i_right():
    correct = ''
    while correct != 'y' and correct != 'n':
        correct = input('Did I guess your number? (y/n)' ).lower()
    if correct == 'y':
        result = True
    else:
        result = False
    return result


def user_input():
    user_in = ''
    while user_in != 'w' and user_in != 'c':
        user_in = input('Am I (w)armer or (c)older? ')
    if user_in == 'c':
        warmer = False
    else:
        warmer = True
    return warmer


def what_to_guess(guess_count, last_guess=0, warm_or_cold=0):
    if guess_count < 1:
        guess = 7
    elif last_guess == 7:
        guess = 3
    elif last_guess == 3 and warm_or_cold:
        guess = 2
    elif last_guess == 2 and warm_or_cold:
        guess = 1
    elif last_guess == 2 and not warm_or_cold:
        guess = 5
    elif last_guess == 5:
        guess = 4
    elif last_guess == 3 and not warm_or_cold:
        guess = 9
    elif last_guess == 9 and warm_or_cold:
        guess = 10
    elif last_guess == 10 and not warm_or_cold:
        guess = 8
    elif last_guess == 8 and warm_or_cold:
        guess = 6
    elif last_guess == 9 and not warm_or_cold:
        guess = 6
    return guess


def game2():
    print('Choose a number between 1 and 10, and I will try to guess it.')
    guess_count = 0
    last_guess = 0
    warm = False
    win = False
    while not win:
        my_guess = what_to_guess(guess_count, last_guess, warm)
        print(my_guess)
        win = am_i_right()
        if win:
            print('I Win!')
            break
        if guess_count > 0:
            warm = user_input()
        last_guess = my_guess
        guess_count += 1


def main():
    game = ''
    while game != 'c' and game != 'y':
        game = input('Would (y)ou like to choose a number, or should the (c)omputer? ')
    if game == 'c':
        game1()
    elif game == 'y':
        game2()


if __name__=='__main__':
    main()