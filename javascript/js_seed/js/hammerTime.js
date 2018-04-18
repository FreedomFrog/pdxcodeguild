// # Breakfast: 7AM - 9AM
// # Lunch: 12PM - 2PM
// # Dinner: 7PM - 9PM
// # Hammer: 10PM - 4AM
//
// hour_str = input("Please enter a time of day (HHAM/HHPM): ").upper()
let time = prompt('What time is it (HH:AM/PM)?');

console.log(time);
// meal_name = ''
// hour = int(hour_str[0:-2])
// am_or_pm = hour_str[-2:]
let time_split = time.split(":")
console.log(time_split)
let hour = parseInt(time_split[0])
let meridian = time_split[1].toLowerCase();
console.log(meridian)
// if am_or_pm == 'AM':
//     if hour in range(7,10):
//         meal_name = 'Breakfast'
//     elif (hour in range(0,5) or hour == 12):
//         meal_name = 'Hammer'
//     else:
//         meal_name = 'not'
//
if ([7,8,9].indexOf(hour) > -1) {
    if (meridian === 'am') {
        console.log("It\'s Breakfast!")
    } else {
        console.log("It\'s Dinner!")
    }
} else if ([12, 1, 2].indexOf(hour) && meridian === 'pm') {
    console.log("It\'s Lunch!")
} else if (hour >= 10 && hour < 12 && meridian === 'pm' || (hour === 12 || [1, 2, 3, 4].indexOf(hour)) && meridian ==='am') {
    console.log("It\'s Hammer Time!")
}
// elif am_or_pm == 'PM' :
//     if (hour <= 2 or hour == 12):
//         meal_name = 'Lunch'
//     elif hour in range(7,10):
//         meal_name = 'Dinner'
//     elif hour in range(10,12):
//         meal_name = 'Hammer'
//     else:
//         meal_name = 'not'
//
// print("It's {} time!".format(meal_name))


