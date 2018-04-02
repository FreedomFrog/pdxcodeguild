class ATM:

    ATM_HISTORY = []

    def __init__(self):
        self.balance = 0
        self.interest_rate = .001

    def check_balance(self):

        return self.balance

    def deposit(self, amount):
        self.ATM_HISTORY.append('user deposit {}'.format(amount))
        self.balance += amount


    def check_withdrawal(self, amount):
        if amount > self.balance:
            result = False
        else:
            return True

    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            result = True
            self.ATM_HISTORY.append('user withdrawal {}'.format(amount))
        else:
            self.ATM_HISTORY.append('user withdrawal attempt {} failed'.format(amount))
            result = False
        return result

    def calc_interest(self):
        return self.balance + (self.balance*self.interest_rate)

    def print_transactions(self):
        print(self.ATM_HISTORY)


def main():
    poss_choice = ['d', 'w', 'c', 'h','quit']
    user_choice = ''
    the_atm = ATM()
    while user_choice != 'quit':
        while user_choice not in poss_choice:
            user_choice = input('What would you like to do (d_eposit, w_ithdraw, c_heck balance, h_istory, or quit)?').lower()

        if user_choice == 'd':
            user_deposit = int(input('How much would you like to deposit? $'))
            the_atm.deposit(user_deposit)
            print('Your deposit of {} has been made'.format(user_deposit))
            user_choice = ''
        elif user_choice == 'w':
            user_withdraw = int(input('How much would you like to withdraw? $'))
            if the_atm.withdraw(user_withdraw):
                print('Your withdrawl of {} has been made'.format(user_withdraw))
                user_choice = ''
            else:
                print('Insufficient funds, must be lower than {}'.format(the_atm.balance))
                user_choice = ''
        elif user_choice == 'c':
            print('Current balance is {}'.format(the_atm.balance))
            user_choice = ''
        elif user_choice == 'h':
            the_atm.print_transactions()
            user_choice = ''


if __name__ == '__main__':
    main()