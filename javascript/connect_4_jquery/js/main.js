function switchPlayer (event) {
    $('#player').toggleClass("red");
    var text = $('#player').text();
    $('#player').text(
        text == "Player 1's Turn"? "Player 2's Turn": "Player 1's Turn");

}

function placePiece (event) {
    let col_num = $(this).attr("id");
    console.log(col_num)
}

$(".place-piece-button").click(placePiece);