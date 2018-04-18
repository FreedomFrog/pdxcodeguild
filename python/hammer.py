# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM

hour_str = input("Please enter a time of day (HHAM/HHPM): ").upper()
meal_name = ''
hour = int(hour_str[0:-2])
am_or_pm = hour_str[-2:]
if am_or_pm == 'AM':
    if hour in range(7,10):
        meal_name = 'Breakfast'
    elif (hour in range(0,5) or hour == 12):
        meal_name = 'Hammer'
    else:
        meal_name = 'not'
        
elif am_or_pm == 'PM' :
    if (hour <= 2 or hour == 12):
        meal_name = 'Lunch'
    elif hour in range(7,10):
        meal_name = 'Dinner'
    elif hour in range(10,12):
        meal_name = 'Hammer'
    else:
        meal_name = 'not'

print("It's {} time!".format(meal_name))
