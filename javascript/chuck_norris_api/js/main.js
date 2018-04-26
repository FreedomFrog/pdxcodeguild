function jokeMe() {
    $.ajax('http://api.icndb.com/jokes/random', {
    success: function (response){
        $('#jokeid').html(response.value.id);
        $('#joketext').html(response.value.joke);
        let el = $('#count');
        let val = parseInt(el.text()) + 1;
        el.text(val);
    }
})
}
$(document).ready(function () {

    $('#press').click(jokeMe)
});

