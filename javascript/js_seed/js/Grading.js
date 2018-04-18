let grade_prec = parseInt(prompt("Enter a grade (0-100): "));

function assign_letter_grade(percent) {
    let letter_grade;
    if (percent >= 90) {
        letter_grade = 'A'
    } else if (percent >= 80) {
        letter_grade = 'B'
    } else if (percent >= 70) {
        letter_grade = 'C'
    } else if (percent >= 60) {
        letter_grade = 'D'
    } else {
        letter_grade = 'F'
    }
    if (percent % 10 < 3) {
        letter_grade = letter_grade.concat('-')
    } else if (95 > percent % 10 > 7) {
        letter_grade = letter_grade.concat('+')
    }
    return letter_grade

}
console.log(assign_letter_grade(grade_prec));