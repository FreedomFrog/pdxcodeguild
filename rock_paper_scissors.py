from random import choice

lst_options = ['rock', 'paper', 'scissors']
def gen_reponse(first_player, second_player):
    outcome = ''
    if first_player == second_player:
        outcome = 'Tie.'
    elif ((first_player == 'rock' and second_player =='paper')
        or (first_player == 'paper' and second_player =='scissors')
        or (first_player == 'scissors' and second_player == 'rock')):
        outcome = 'You lose.'
    else:
        outcome = 'you win!'
    return 'You played {}, I played {}...{}'.format(first_player, second_player, outcome)
user_play = ''
while True:
    while user_play != 'rock' and user_play != 'paper' and user_play != 'scissors':
        user_play = input('Enter Rock, Paper, or Scissors: ').lower()
    comp_play = choice(lst_options)
    print(gen_reponse(user_play, comp_play))
    stay_or_quit = input('Would you like to continue (y/n)?: ')
    user_play = ''

    if stay_or_quit == 'n':
        print('Good bye')
        break
