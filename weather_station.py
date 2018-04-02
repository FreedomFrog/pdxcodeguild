import requests
import string


def is_celcius():
    user_in = ''
    while user_in != 'c' and user_in !='f':
        user_in = input('(C)elsius or (F)ahrenheit?: ').lower()
    if user_in == 'c':
        result = True
    else:
        result = False
    return result


def get_zip_city():
    user_in = input('Enter a city name or 5 digit zipcode: ')
    if user_in[0] in string.digits:
        user_type = 'zip'
    else:
        user_type = 'q'
    return user_type, user_in


def convert_from_k(degrees, c_f):
    if c_f:
        degrees = degrees - 273.15

    else:
        degrees = (9 / 5) * (degrees - 273) + 32

    return round(degrees, 2)


def api_call(call_type, call_value, units):
    if units:
        will_celsius = 'metric'
    else:
        will_celsius = 'imperial'

    package = {
        'APPID': '13a106022d63ffd4ff4668b6cad93dc1',
        call_type: call_value,
        'units': will_celsius
    }

    r = requests.post('https://api.openweathermap.org/data/2.5/weather', params=package)
    return r.json()


def get_rel_info(api_req, c_f):
    weather = {'main': api_req['weather'][0]['main'],
               'description': api_req['weather'][0]['description'],
               'temp': api_req['main']['temp']}
    #weather['temp'] = convert_from_k(weather['temp'], c_f)
    return weather


def main():
    a_bool = is_celcius()
    a_zip_or_city, value = get_zip_city()
    weather = api_call(a_zip_or_city, value, a_bool)
    results = get_rel_info(weather, a_bool)
    print('The current weather in {} is {} ({}) and {} degrees.'.format(value, results['main'], results['description'], results['temp']))


if __name__ == "__main__":
   main()