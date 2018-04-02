import requests
import datetime
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def pull_web_data():
    url = 'https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain'

    r = requests.get(url).text

    with open('rain_data.txt', 'w') as f:
        f.write(r)

def read_file_data():
    file = 'rain_data.txt'
    data_dict = {}
    with open(file) as f:
        content = f.readlines()
        for line in content[:9]:
            pass
        for line in content[11:]:
            data = line.split()
            data_dict[data[0]] = {'total':data[1]}
            for index, value in enumerate(data[2:]):
                if value.isdigit():
                    data_dict[data[0]][index] = int(value)
    return data_dict


def find_mean(dict_data):
    total = 0
    for key, value in dict_data.items():
        if dict_data[key]['total'] != '-':
            total += int(dict_data[key]['total'])
    avg_mean = total / len(dict_data)
    return avg_mean


def convert_to_date(a_str):
    date = datetime.datetime.strptime(a_str, '%d-%b-%Y')
    return date


def yearly_rain_dict(data_dict):
    year_total_rain_dict = {}
    for key, value in data_dict.items():
        date = convert_to_date(key)
        if data_dict[key]['total'] != '-':
            if date.year in year_total_rain_dict:
                year_total_rain_dict[date.year] = int(data_dict[key]['total']) + int(year_total_rain_dict[date.year])
            else:
                year_total_rain_dict[date.year] = int(data_dict[key]['total'])
    return year_total_rain_dict

def monthly_rain_dict(data_dict):
    month_total_rain_dict = {}
    for key, value in data_dict.items():
        date = convert_to_date(key)
        if data_dict[key]['total'] != '-':
            if date.month in month_total_rain_dict:
                month_total_rain_dict[date.month] += int(data_dict[key]['total'])
            else:
                month_total_rain_dict[date.month] = int(data_dict[key]['total'])
    return month_total_rain_dict

def most_rain_day(data_dict):
    max_rain_day = max(data_dict, key=lambda key: data_dict[key]['total'])
    return max_rain_day


def most_rain_year(data_dict):
    year_total_dict = yearly_rain_dict(data_dict)
    max_rain_year = max(year_total_dict, key=lambda key: year_total_dict[key])
    return max_rain_year


def plot_total_rain_year(big_data_dict):
    x_axis = []
    y_axis = []
    data_dict = yearly_rain_dict(big_data_dict)
    for key, value in data_dict.items():
        x_axis.append(key)
        y_axis.append(value)
    plt.scatter(x_axis, y_axis)
    plt.xlabel('Year')
    plt.ylabel('Total inches')
    plt.xlim(min(x_axis), max(x_axis))
    print(x_axis)
    print(y_axis)
    plt.show()


def plot_all_rainfall(big_data_dict):
    x_axis = []
    y_axis = []
    for key, value in big_data_dict.items():
        if big_data_dict[key]['total'] != '-':
            date = convert_to_date(key)
            total_rain = big_data_dict[key]['total']
            x_axis.append(date)
            y_axis.append(int(total_rain))
    #plt.plot(x_axis, y_axis)
    #plt.xlim(min(x_axis), max(x_axis))
    #plt.show()
    dates = matplotlib.dates.date2num(x_axis)
    plt.plot_date(dates, y_axis)
    plt.yticks(np.arange(0,300,50))
    plt.show()


def main():
    data = read_file_data()
    avg_data = find_mean(data)
    print(avg_data)
    print(most_rain_day(data))
    print(most_rain_year(data))
    plot_total_rain_year(data)
    plot_all_rainfall(data)


if __name__=='__main__':
    main()