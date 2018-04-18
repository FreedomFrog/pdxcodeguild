let playing = true;
while (playing) {


    let com_play = Math.floor(Math.random() * 3) + 1;

    let usr_play = prompt("Rock, Paper, Scissors: ").toLowerCase();

    function convert_usr_play(a_str) {
        let play_val_dict = {
            'rock': 1,
            'paper': 2,
            'scissors': 3
        };
        return play_val_dict[a_str]
    }

    com_play === convert_usr_play(usr_play) ? console.log('Tie') : com_play - convert_usr_play(usr_play) === -1 || com_play - convert_usr_play(usr_play) === 2 ? console.log('You win!') : console.log('You lose');
    console.log(com_play);
    console.log(usr_play);
    let cont_play = prompt("play again? (y/n): ").toLowerCase();
    cont_play === 'n' ? playing = false: playing = true;
}