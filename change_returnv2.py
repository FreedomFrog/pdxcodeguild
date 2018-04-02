dollar_values = [100, 50, 20, 10, 5, 1]
coin_values = [25, 10, 5, 1]
dollars_in_till = [0,0,0,0,0,0]
coins_in_till = [0,0,0,0]


coin_names_dict = {'25':'quarter', '10':'dime', '5':'nickel', '1':'penny'}

def load_till():
    for index, value in enumerate(dollar_values):
        user_input = input("How many {}'s in till? ".format(value))
        dollars_in_till[index] = int(user_input)
    for index, value in enumerate(coin_values):
        coin_name = coin_names_dict[str(value)]
        user_input = input("How many {}s in till? ".format(coin_name))
        coins_in_till[index] = int(user_input)



def check_dollar_in_till(amount):
    for index, value in enumerate(dollars_in_till):
        if value > 0:
            if (value * dollar_values[index]) > amount:
                amount = amount % dollar_values[index]
            else:
                amount = amount - (value * dollar_values[index])
    return amount


def check_coin_in_till(amount):
    for index, value in enumerate(coins_in_till):
        if value > 0:
            if (value * coin_values[index]) > amount:
                amount = amount % coin_values[index]
            else:
                amount = amount - (value * coin_values[index])
    return amount

def make_change(dollars, cents):
    change_to_pay = [0,0,0,0,0,0,0,0,0,0]
    for index, value in enumerate(dollar_values):
        num_dollars = dollars // value
        if num_dollars > dollars_in_till[index]:
            dollars = dollars - (dollars_in_till[index] * dollar_values[index])
            dollars_in_till[index] = 0
        else:
            dollars = dollars - (num_dollars * dollar_values[index])
            dollars_in_till[index] = dollars_in_till[index] - num_dollars
        change_to_pay[index] = num_dollars
    for index, value in enumerate(coin_values):
        num_cents = cents // value
        if num_dollars > dollars_in_till[index]:
            cents = cents - (coins_in_till[index] * coin_values[index])
            coins_in_till[index] = 0
        else:
            cents = cents - (num_cents * coin_values[index])
            coins_in_till[index] = coins_in_till[index] - num_cents
        change_to_pay[index + 6] = num_cents
    return change_to_pay

def gen_output(lst_tender):
    for index, value in enumerate(lst_tender):
        if index < 6 and value > 0:
            print('Provide {} ${}s from the till'.format(value, dollar_values[index]))
        if index >= 6 and value > 0:
            print('Provide {} {} from the till'.format(value, coin_names_dict[str(coin_values[index - 6])]))


def transaction():
    while True:
        user_str = input('Enter change to be dispensed: $')
        result = user_str.split('.')
        dollars = int(result[0])
        cents = int(result[1])
        missing_dollars = check_dollar_in_till(dollars)
        missing_cents = check_coin_in_till(cents)
        if missing_dollars > 0 or missing_cents > 0:
            print('missing_dollars{}'.format(missing_dollars))
            print('missing_cents{}'.format(missing_cents))
            print("Till requirements not met!\nLoad till and redo transaction...")
            load_till()
            continue
        lst_payment = make_change(dollars, cents)
        print(lst_payment)
        gen_output(lst_payment)



the_till = load_till()
print(the_till)
transaction()
