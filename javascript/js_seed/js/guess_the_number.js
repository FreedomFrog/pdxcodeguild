let user_guess_count = 0;

let computer_guess = Math.floor(Math.random() * 10) + 1;

console.log(computer_guess);

let playing = true;

let user_guess;

while (user_guess_count < 7) {
    console.log('hi');
    user_guess = parseInt(prompt('What is your guess?'));
    user_guess_count ++
    if (user_guess > computer_guess) {
        console.log('greater')
    } else if (user_guess < computer_guess) {
        console.log('You guessed too low!')
    } else {
        console.log(`YOU GUESSED IT!! YAY!!! you guessed it in ${user_guess_count}`)
        break
    }
}