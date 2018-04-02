import math
import sys


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


def compute_ari(c_dict):
    ari = math.ceil(4.71 * (c_dict['characters']/c_dict['words']) + 0.5 * (c_dict['words']/c_dict['sentences']) - 21.43)

    return ari

def open_read_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    return text


def count_stats(text):
    stats_dict = {}
    split_text = text.split()
    sentences = text.split('.')
    sentences = [sentence for sentence in sentences if len(sentence) > 2]
    stats_dict['words'] = len(split_text)
    stats_dict['characters'] = len(text)
    stats_dict['sentences'] = len(sentences)
    return stats_dict



def gen_print_out(ari_int, str_file):
    ari_adj = ari_int
    if ari_int > 14:
        ari_adj = 14
    print('-' * 54)
    print()
    print('The ARI for {} is {}'.format(str_file, ari_int))

    print('This corresponds to a {} of difficulty'.format(ari_scale[ari_adj]['grade_level']))
    print('that is suitable for an average person {} years old'.format(ari_scale[ari_adj]['ages']))
    print()
    print('-' * 54)

def main(arg):
    path = arg
    text = open_read_file(path)
    stats = count_stats(text)
    ari = compute_ari(stats)
    gen_print_out(ari, path)


if __name__ == '__main__':
    main(sys.argv[1])