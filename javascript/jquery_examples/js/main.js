//JQuery

$('#submit').click(function (e) {
    attachListItem($('#toDoInput').val())
});

$('#toDoInput').keypress(function (e) {
    if (e.keyCode === 13) {
        attachListItem($(this).val())
    }
});

function attachListItem(item) {
    console.log(item)
}