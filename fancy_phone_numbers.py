usr_str = input('Please enter an all digits phone number. >> ')
ret_str = '(' + usr_str[0:3] + ') ' + usr_str[3:6] + '-' + usr_str[6:]
print(ret_str)
