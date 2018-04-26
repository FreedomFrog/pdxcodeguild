$(document).ready(function () {
    $('#play-button').on('click', play);

    function roll() {
        return Math.floor(Math.random() * 6) + 1;
    }

    function clear_holds () {
        $('#hold-1').removeClass('holding');
        $('#hold-2').removeClass('holding');
    }

    function winCond(r_num, die1, die2) {
        console.log(r_num)
        console.log(die1)
        console.log(die2)
        if (die1 === 3 && die2 === 3) {
            clear_holds();
            return 1
        }
        else {
            if (r_num === 1) {
                if (die1 === 1 && die2 === 2 || die1 === 2 && die2 === 1) {
                    clear_holds();
                    return 2
                } else {
                    return r_num
                }
            }
            else if (r_num === 2) {
                if (die1 === 2 && die2 === 3 || die1 === 3 && die2 === 2) {
                    clear_holds();
                    return 3
                } else {
                    return r_num
                }
            }
            else if (r_num === 3) {
                if (die1 === 5 && die2 === 6 || die1 === 6 && die2 === 5) {
                    clear_holds();
                    return 4
                } else {
                    return r_num
                }
            }
        }
    }

    function showDice(d_val) {
        if (d_val === 3) {
            return 'angry.png'
        }
        else {
            return `${d_val}.png`
        }
    }

    function new_roll(event) {
        if ($('#hold-1').hasClass('holding')) {
            var dieOne = $('#die-1').attr('data-die');
        } else {
            var dieOne = roll();
            $('#die-1').attr("data-die", dieOne)
        }
        if ($('#hold-2').hasClass('holding')) {
            var dieTwo = $('#die-2').attr('data-die')
        } else {
            var dieTwo = roll();
            $('#die-2').attr("data-die", dieTwo)
        }

        $('#die-1').empty();
        $('#die-2').empty();
        $('#die-1').append(`<img class="img" src="img/${showDice(dieOne)}">`);
        $('#die-2').append(`<img class="img" src="img/${showDice(dieTwo)}">`);
        let this_round = $('#round-num').attr('data-round');
        console.log(this_round);
        console.log(dieOne);
        console.log(dieTwo);
        this_round = winCond(this_round, dieOne, dieTwo);
        $('h2').attr('data-round', this_round);
        $('h2').text(`Round ${this_round}`)
    }
    console.log(winCond(1,"1","2"))

    function play(event) {
        let dieOne = roll();
        let dieTwo = roll();
        let round = 1;

        $('#play').css({'display': 'none'});
        $('h2').attr('data-round', round);
        $('#round-num').text(`Round ${round}`);
        $('#die-1').append(`<img src="img/${showDice(dieOne)}">`)
        .attr('data-die', dieOne);
        $('#die-2').append(`<img src="img/${showDice(dieTwo)}">`)
        .attr('data-die', dieTwo);
        $('.hold-button').on('click', function () {
            $(this).toggleClass('holding')
        })
        $('#roll-button').on('click', new_roll);
        $('#dice').on('click', function (event) {
            if ($(this).class === "hold-button") {
                $(this).closest("hold-button").attr('data-value',1)
            }
        })




    }
});