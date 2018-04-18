grade_as_number_string = input("Enter a number representing the grade (0-100): ")
grade_as_number_float = float(grade_as_number_string)
grade_as_string = ''

def lettergrade(float_grade):
    grade = ''
    if float_grade >= 90:
        grade = 'A'
    elif float_grade >= 80:
        grade = 'B'
    elif float_grade >= 70:
        grade = 'C'
    elif float_grade >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade


if grade_as_number_float == 100:
    print(lettergrade(grade_as_number_float) + '+')
elif (grade_as_number_float % 10 < 2) and grade_as_number_float > 50:
    print(lettergrade(grade_as_number_float) + '-')
elif (grade_as_number_float % 10 >= 8) and grade_as_number_float > 40:
    print(lettergrade(grade_as_number_float) + '+')
else:
    print(lettergrade(grade_as_number_float))
