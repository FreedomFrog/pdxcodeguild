ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'
}
tens = {
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}
teens = {
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}
deci_dict = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}
deci_value = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

def get_num():
    num_str = ''
    while not num_str.isdigit():
        num_str = input("Enter a digit to convert to english: ")
    return int(num_str)

def arabic_or_roman():
    a_or_r = input('Would you like to convert from arabic to roman? (y/n): ').lower()
    return a_or_r

def arabic_to_english(digit):
    ones_digit = digit%10
    tens_digit = digit//10%10
    hund_digit = digit//100%10
    assembled_lst = []
    if hund_digit > 0:
        assembled_lst.append(ones[hund_digit])
        assembled_lst.append('hundred')
        if tens_digit > 0 or ones_digit > 0:
            assembled_lst.append('and')
    if tens_digit == 1:
        if ones_digit == 0:
            assembled_lst.append(tens[tens_digit])
        else:
            assembled_lst.append(teens[ones_digit])

    elif tens_digit > 1:
        assembled_lst.append(tens[tens_digit])

    if ones_digit > 0 and tens_digit != 1:
        assembled_lst.append(ones[ones_digit])
    elif ones_digit == 0 and tens_digit == 0 and hund_digit == 0:
        assembled_lst = [ones[ones_digit]]

    return " ".join(assembled_lst)


def arabic_to_roman(digit):
    assembled_lst = []
    if digit in deci_value:
        assembled_lst.append(deci_dict[digit])
    else:
        while digit > 0:
            high_val = [i for i in deci_value if i <= digit][-1]
            highest_rom = deci_dict[high_val]
            assembled_lst.append(highest_rom)
            digit -= high_val
    return ''.join(assembled_lst)


def main():
    num_to_conv = get_num()
    str_ret = arabic_to_english(num_to_conv)
    print(str_ret.capitalize())
    str_ret_rom = arabic_to_roman(num_to_conv)
    print(str_ret_rom)



if __name__=='__main__':
    main()