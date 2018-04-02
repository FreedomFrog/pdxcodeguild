def get_digits():
    card_number = ''
    while not card_number.isdigit():
        card_number = input('Please enter card number: ')
    num_list = [int(i) for i in card_number]
    return num_list


def validate_card(digits):
    a_bool = False
    print(digits)
    copy_dig = digits[:]
    print(copy_dig)
    check_dig = copy_dig.pop()
    print(check_dig)
    print(copy_dig)
    copy_dig = copy_dig[::-1]
    print(copy_dig)
    copy_dig[::2] = [x * 2 for x in copy_dig[::2]]
    print(copy_dig)
    copy_dig = [x if x <= 9 else x - 9 for x in copy_dig]
    print(copy_dig)
    total = sum(copy_dig[:])
    total = total % 10
    print(total)
    if total == check_dig:
        a_bool = True
    return a_bool


def main():
    digits = get_digits()
    valid = validate_card(digits)
    print(valid)
    if valid:
        print('This card is valid.')
    else:
        print('This card is invalid.')


if __name__ == '__main__':
    main()