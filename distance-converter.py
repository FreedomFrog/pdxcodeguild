dict_of_dist_conv = {
'mi_m': 1609.344,
'mi_km': 1.609344,
'mi_ft': 5280,
'mi_in': 63360
'mi_cm': 160934
'km_ft': 3280.839895,
'km_m': 1000,
'km_mi': 0.62137,
'km_in': 39370.1
'km_cm': 100000
'ft_m': 0.3048037064,
'ft_km': 0.000304803,
'ft_mi': 0.000189393939,
'ft_in': 12
'ft_cm': 30.48
'in_m': 0.0254
'in_mi': 0.0000157828,
'in_km': 0.0000254,
'in_ft': 0.083333,
'in_cm': 2.54,
'cm_m': 0.01
'cm_mi': 0.0000062137,
'cm_km': 0.00001,
'cm_ft': 0.0328084,
'cm_in': 0.393701
}
dict_of_vol_conv = {
'gal_l': 3.7854,
'l_gal': 0.2641728747
}

def get_user_input():
    dis = input('Enter a distance: \n')
    uni = input('Enter units: \n')
    tar_uni = input('Enter target units: \n')
    return [dis, uni, tar_uni]

def check_user_input():
    check_user = True
    while check_user:
        user_input = get_user_input()
        conv = str(user_input[1] + '_' + user_input[2])
        if conv in dict_of_dist_conv:
            user_input.append(dict_of_dist_conv[conv])
            check_user = False
        elif conv in dict_of_vol_conv:
            user_input.append(dict_of_vol_conv[conv])
            check_user = False
        else:
            raise NameError('Not a possible conversion')


    return user_input
def gen_output(user_list_checked):

    conv_units = user_list_checked[3] * float(user_list_checked[0])

    result = '{} {} is {} {}'.format(user_list_checked[0], user_list_checked[1], conv_units, user_list_checked[2])
    return result

alist = check_user_input()
print(gen_output(alist))
