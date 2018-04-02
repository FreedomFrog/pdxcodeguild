import string


def make_letter_map():
    letter_dict = {}
    for index, letter in enumerate(string.ascii_lowercase):
        letter_dict[letter] = index
    return letter_dict


def rotate_cipher(int_rot):
    base = make_letter_map()
    cipher = {}
    for key, value in base.items():
        value = (value + int_rot) % 26
        cipher[value] = key
    return cipher


def get_user_str():

    user_in_cypher = input('Enter integer to use for cipher: ')

    user_in = input('Enter string to encrypt (no spaces): ').lower()

    return int(user_in_cypher), user_in


def make_cipher(a_str, a_dict):
    let_map = make_letter_map()
    scrabbled = []
    for letter in a_str:
        value = let_map[letter]
        lett = a_dict[value]
        scrabbled.append(lett)
    return scrabbled


def main():
    an_int, a_string = get_user_str()
    a_cipher = rotate_cipher(an_int)
    scram_lst = make_cipher(a_string, a_cipher)
    print(''.join(scram_lst))


if __name__ == "__main__":
    main()