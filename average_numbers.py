import string

def get_user_nums():
    user_in = ''
    nums = []
    while user_in != 'done':
        user_in = input('enter a number, or "done" to get average: ')
        if user_in.isdigit():
            nums.append(int(user_in))
    return nums

def get_lst_avg(a_list):
    avg = round(sum(a_list)/len(a_list), 2)
    return avg


def main():
    lst_num = get_user_nums()
    print('average: {}'.format(get_lst_avg(lst_num)))


if __name__ == "__main__":
   main()