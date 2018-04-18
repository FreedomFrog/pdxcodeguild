import string

lst_lower = list(string.ascii_lowercase)
lst_punc = list(string.punctuation)
lst_upper = list(string.ascii_uppercase)
lst_vowel = ['a', 'e', 'i', 'o', 'u', 'y']

def get_input():
    word = input('Word?: ')
    return word

def is_punct(char):
    result = False
    if char in lst_punc:
        result = True
    return result

def is_lower(char):
    result = False
    if char in lst_lower:
        result = True
    return result

def is_upper(char):
    result = False
    if char in lst_upper:
        result = True
    return result

def is_vowel(char):
    result = False
    if char.lower() in lst_vowel:
        result = True
    return result

def find_first_vowel(word):
    result = 100
    for index, letter in enumerate(word):
        if is_vowel(letter):
            result = index

            break
    return result

def rearrange_word(index, word):
    if index == 0:
        word = '{}yay'.format(word)
    else:
        word = word[index:] + word[0:index] + 'ay'
    return word

def check_for_upper(word):
    result = False
    for letter in word:
        if letter in lst_upper:
            result = True
    return result

def check_for_punc(word):
    result = False
    for letter in word:
        if letter in lst_punc:
            result = True
    return result

def clean_word(word):
    cln_word = ''
    punc =[]
    for letter in word:
        if letter in lst_punc:
            punc = punc.append(letter)
        else:
            cln_word += letter
    return cln_word, punc

def make_pig_word(word):
    an_index = find_first_vowel(word)
    pig_word = rearrange_word(an_index, word)
    if check_for_upper(word):
        pig_word = pig_word.captitalize()
    if check_for_punc(word):
        pig_word, punc = clean_word(word)
        pig_word = pig_word + str[punc]
    return pig_word

def gen_output(word, pig_word):
    return '{} in Pig Latin is {}'.format(word, pig_word)

usr_str = get_input()
pig_lat_word = make_pig_word(usr_str)
print(gen_output(usr_str, pig_lat_word))
