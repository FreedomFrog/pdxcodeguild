import sys
import string
import re
import random


def remove_head_foot(path):
    re.compile('[*]+[a-zA-Z0-9_]+[*]+([a-zA-Z0-9_]+)[*]+[a-zA-Z0-9_]+[*]+')
    pass


def book_reader(path):
    with open(path, 'r', encoding='utf-8') as book:
        full_text = book.read()
        full_text = full_text.lower()
        cleaned_text = ''
        for char in full_text:
            if char in string.ascii_letters + ' ':
                cleaned_text += char
            else:
                cleaned_text += ' '
    return cleaned_text


def word_counter(string_of_words):
    list_of_words = string_of_words.split(' ')
    word_count_dict = {}
    for word in list_of_words:
        if word == '':
            pass
        elif word not in word_count_dict:
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1
    return word_count_dict


def find_max_count(a_dict, an_int):
    sorted_top_count = sorted(list(a_dict.items()), key=lambda x: x[1], reverse=True)
    max_lst = sorted_top_count[:an_int]
    return max_lst


def word_follower(string_of_words):
    list_of_words = string_of_words.split(' ')
    word_dict = {}
    for index, word in enumerate(list_of_words):
        if index < len(list_of_words) - 1:
            next_word = list_of_words[index + 1]
        else:
            break
        if word == '' or next_word == '':
            pass
        elif len(word) > 0:
            if word not in word_dict:
                word_dict[word] = {}
            if next_word not in word_dict[word]:
                word_dict[word][next_word] = 1
            else:
                word_dict[word][next_word] += 1
    return word_dict


def word_follower_norm(a_dict):
    normed_dict = {}
    for keys, word_dict in a_dict.items():
        total_count = 0
        for key, value in word_dict.items():
            total_count += value
        for new_key, new_value in word_dict.items():
            new_value = new_value / total_count
            if keys in normed_dict:
                normed_dict[keys].update({new_key: new_value})
            else:
                normed_dict[keys] = {new_key: new_value}
    return normed_dict


def possibilities(word, normed_dict):
    sorted_values = sorted(list(normed_dict[word].items()), key=lambda x: x[1], reverse=True)
    print(sorted_values)


def word_randomizer(word_list):
    rand_val = random.random()
    total = 0
    for k, v in word_list.items():
        total += v
        if rand_val <= total:
            return k
    assert False, 'unreachable'


def sentence_maker(word, normed_dict, arg):
    list_of_words = [word]
    length_of_sentence = 10
    i = 0
    while i < length_of_sentence:
        word_to_match = list_of_words[i]

        if word_to_match not in normed_dict:
            rand_int = random.randint(0, 9)
            a_top_word = find_max_count(word_counter(book_reader(arg)), 10)[rand_int][0]
            add_word_dict = normed_dict[a_top_word]
        else:
            add_word_dict = normed_dict[word_to_match]

        list_of_words.append(word_randomizer(add_word_dict))
        i += 1
    return ' '.join(list_of_words)


def main(args):
    for arg in args:
        clean_str = book_reader(arg)
        word_count = word_counter(clean_str)
        top_words = find_max_count(word_count, 10)
        print('For the book {} \nThe top {} words are: {}'.format(arg, 10, top_words))

        follower_dict = word_follower(clean_str)
        normed_follower_dict = word_follower_norm(follower_dict)
        while True:
            prompt_user = input('Enter a word: ')
            if prompt_user in normed_follower_dict:
                break
            print('Not in book, try again.')
        print(sentence_maker(prompt_user, normed_follower_dict, arg))


if __name__ == "__main__":
   main(sys.argv[1:])