$(document).ready(function () {

    function dice_val() {
        return Math.floor(Math.random() * 6) + 1;
    }

    function showDice(d_val) {
        if (d_val == 3) {
            return `<img class="img" src="img/angry.png">`;
        }
        else {
            return `<img class="img" src="img/${d_val}.png">`;
        }
    }

    function check_holding (dieOne, dieTwo) {
        if ($('#hold-1').hasClass('holding')) {

        } else {
            $('#die-1').empty();
            dieOne = dice_val();
            $('#die-1').append(showDice(dieOne));
            $('#die-1').attr("die_val", dieOne);
        }
        if ($('#hold-2').hasClass('holding')) {

        } else {
            $('#die-2').empty();
            dieTwo = dice_val();
            $('#die-2').append(showDice(dieTwo));
            $('#die-2').attr("die_val", dieTwo);
        }
    }

    function clearHold() {
        $('#hold-1').removeClass('holding');
        $('#hold-2').removeClass('holding');
    }

    function check_round_win() {
        let r_num = $('#round-num').attr("round");
        let dieOne_val = $('#die-1').attr("die_val");
        let dieTwo_val = $('#die-2').attr("die_val");

        if (dieOne_val == 3 && dieTwo_val == 3) {
            $('#round-num').attr("round", 1);
            $('#round-num').text(`Round ${$('#round-num').attr("round")}`)
        } else {
            if (r_num == 1) {
                if (dieOne_val == 1 && dieTwo_val == 2 || dieOne_val == 2 && dieTwo_val == 1) {
                    clearHold()
                    $('#round-num').attr("round", 2);
                }
            } else if (r_num == 2) {
                if (dieOne_val == 3 && dieTwo_val == 4 || dieOne_val == 4 && dieTwo_val == 3) {
                    clearHold()
                    $('#round-num').attr("round", 3);
                }
            } else if (r_num == 3) {
                if (dieOne_val == 5 && dieTwo_val == 6 || dieOne_val == 6 && dieTwo_val == 5) {
                    clearHold()
                    $('#round-num').attr("round", 'win');
                    $('#play').css({'display': 'block'})

                }
            }
        }
    }

    function roll () {
        let dieOne_val = $('#die-1').attr("die_val");
        let dieTwo_val = $('#die-2').attr("die_val");
        check_holding(dieOne_val, dieTwo_val);
        check_round_win();
        $('#round-num').text(`Round ${$('#round-num').attr("round")}`)


    }

    function hold (event) {
        if ($(this).id == "hold-1" && $('#die-1').attr("die-val") == 6) {
            alert("Cannot hold 6");
        }
        else if ($(this).id == "hold-2" && $('#die-2').attr("die-val") == 6) {
            alert("Cannot hold 6");
        }
        else {
            $(this).toggleClass('holding')
        }
    }

    function play (event) {
        $('#play').css({'display': 'none'});
        $('#die-1').attr("die_val", dice_val());
        $('#die-2').attr("die_val", dice_val());
        $('#die-1').append(showDice($('#die-1').attr("die_val")));
        $('#die-2').append(showDice($('#die-2').attr("die_val")));
        $('#round-num').attr("round", 1);
        $('#round-num').text(`Round ${$('#round-num').attr("round")}`)

    }

    $('#HOLD1-button').on('click', hold);
    $('#HOLD2-button').on('click', hold);
    $('#roll-button').on('click', roll);
    $('#play-button').on('click', play);


    });