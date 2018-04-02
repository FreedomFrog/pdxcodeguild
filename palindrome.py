import string

is_digit = list(string.digits)
is_punctuation = list(string.punctuation)

def clean_input(in_str):
    cln_str = in_str
    for value in is_digit:
        cln_str = cln_str.replace(str(value), '')
    for value in is_punctuation:
        cln_str = cln_str.replace(str(value), '')
    return cln_str

def reverse_str(in_str):
    rev_str = ''.join(list(reversed(in_str)))
    return rev_str

def get_input():
    in_str = input('Enter a word to check if it is a palindrome: ').lower()
    return in_str

def gen_output(a_str, a_bool):
    out_string = '{} is not a palindrome'.format(a_str)
    if a_bool:
        out_string = '{} is a palindrome.'.format(a_str)
    return out_string


def check_palindrome(cln_str, rev_cln_str):
    result = False
    if cln_str == rev_cln_str:
        result = True
    return result

def palindrome_checker():
    us3r_str = get_input()
    cleaned_usr_str = clean_input(us3r_str)
    rev_c_u_s = reverse_str(cleaned_usr_str)
    a_bool = check_palindrome(cleaned_usr_str, rev_c_u_s)
    output = gen_output(cleaned_usr_str, a_bool)
    print(output)

palindrome_checker()
