from math import ceil
# Assume one gallon of paint covers 400 square feet.
#
# Ask the user for:
#
# Width of the wall
# Height of the wall
# How much a gallon of paint costs
# Figure out then print how much it will cost to paint the wall with one coat.

def get_user_input():
    num_of_walls = input('How many walls?: ')
    coats = input('How many coats per wall?: ')
    price_per_gallon = input('Price of a gallon of paint: $')
    user_input_list = [int(num_of_walls), int(coats), float(price_per_gallon),[] ]
    for i in range(int(num_of_walls)):
        w_wall = input('Width of wall {}: '.format(i + 1))
        h_wall = input('Height of  wall {}: '.format(i + 1))
        user_input_list[3].append([float(w_wall),float(h_wall)])

    return user_input_list

def calc_total_wall_area(lst_of_dims):
    total_wall_area = 0
    for wall in lst_of_dims:
        wall_area = wall[0] * wall[1]
        total_wall_area += wall_area
    return total_wall_area

def calc_total_cost(user_gen_list):
    lst_dim_walls = user_gen_list[3][:]
    area = calc_total_wall_area(lst_dim_walls)
    total_area = user_gen_list[1] * area
    total_paint = ceil(total_area/400)
    total_cost = total_paint * user_gen_list[2]
    return total_cost



user_data = get_user_input()
print(user_data)
total = calc_total_cost(user_data)
print('Your total cost is {}'.format(total))
