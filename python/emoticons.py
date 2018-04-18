from random import choice

lst_of_eyes = [';',':','B','8','=','X']
lst_of_noses = ['-','','>','<','o']
lst_of_mouths = [')','(','?','/','|','\\','}','{']

i = 0

while i < 5:
    print('{}{}{}'.format(
        choice(lst_of_eyes), choice(lst_of_noses), choice(lst_of_mouths)))
    print(' ')
    i += 1
