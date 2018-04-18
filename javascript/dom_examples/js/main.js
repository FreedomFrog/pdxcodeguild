document.querySelector("#mainTitle").addEventListener('mouseout', function (e) {
    document.querySelector("#mainTitle").style.backgroundColor = null
});

let color = 'blue';

function get_color() {
    let new_color;
        new_color = document.querySelector("#color-picker").value;
        console.log(new_color)
    color = new_color;
    }

document.querySelector("#color-picker").addEventListener('change', get_color);

document.querySelector("#mainTitle").addEventListener('mouseover', function (e) {
    document.querySelector("#mainTitle").style.backgroundColor = color
});