from random import choice

choices = ["It is certain", "It is decidedly so",
"Without a doubt", "Yes definitely",
"You may rely on it", "As I see it, yes",
"Most likely", "Outlook good",
"Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later",
"Better not tell you now", "Cannot predict now",
"Concentrate and ask again", "Don’t count on it",
"My reply is no", "My sources say no",
"Outlook not so good", "Very doubtful"]



def welcome():
    print("*" * 23)
    print("*" + " "*3 + 'MAGIC EIGHTBALL' + " "*3 + "*")
    print("*" * 23)

def magic():
    print(".......................")
    print('{}'.format(choice(choices)))
    print(".......................")


def game():
    stay_or_play = 'y'
    welcome()
    while True:
        if stay_or_play == 'y':
            question = input("What would you like to know?: ")
            magic()
            stay_or_play = input('Would you like to continue (y/n)?: ')

        elif stay_or_play == 'n':
            print('Good bye')
            break

        else:
            print('Please enter y or n')

game()
