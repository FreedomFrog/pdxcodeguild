def get_user_input():
    eval_str = ''
    print('(quit) at any time')
    while eval_str != 'quit':
        eval_str = input('Enter equation: ')
        print(eval(eval_str))





def main():
    usr_in = get_user_input()


if __name__ == '__main__':
    main()