from random import choice, randrange
import string
dict_list = {
    '1' : list(string.ascii_lowercase),
    '2' : list(string.ascii_uppercase),
    '3' : list(string.digits),
    '4' : list(string.punctuation)
}

def user_def_reqs():
    pass_len = input("Password length: ")
    pass_lower = input("What is the minimum number of lowercase letters?: ")
    pass_upper = input("What is the minimum number of uppercase letters?: ")
    pass_numbers = input("What is the minimum number of numbers?: ")
    pass_special = input("What is the minimum number of special characters?: ")
    requirement_list = [int(pass_len), int(pass_lower), int(pass_upper),
        int(pass_numbers), int(pass_special)]
    return requirement_list

def check_pass_reqs():
    req_list = user_def_reqs()
    while True:
        if req_list[0] < sum(req_list[1:4]):
            print('Password length must be greater than sum of requirements')
            req_list = user_def_reqs()
        elif req_list[0] >= sum(req_list[1:4]):
            return req_list


def pass_gen(req_list):
    i = 0
    gen_pass = ''
    while int(req_list[0]) > len(gen_pass):
        this_req = randrange(1,5)
        if req_list[this_req] != 0:
            req_list[this_req] -= 1
            gen_pass = gen_pass + choice(dict_list[str(this_req)])
        elif req_list[1:5] == [0,0,0,0]:
            gen_pass = gen_pass + choice(dict_list[str(this_req)])
    return gen_pass

get_input = check_pass_reqs()

password = pass_gen(get_input)
print(password)
