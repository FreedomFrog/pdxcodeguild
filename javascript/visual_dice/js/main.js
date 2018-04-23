function get_dice_roll_value(sides = document.querySelector('#side-count').value) {
    return Math.floor(Math.random() * sides) + 1;
}

function show_sum_html(total) {
    clear_display_sum();
    let the_div = document.querySelector('#display_sum');
    let para = document.createElement('p');
    let para_text = document.createTextNode(total);
    let entry = para.appendChild(para_text);
    the_div.appendChild(entry);
}

function show_dice(arr) {
    for (let face in arr) {
        // let die = document.createElement('div',{'id': face.toString(), 'value': arr[face].toString()})
        // die.appendChild(document.createTextNode(arr[face]))
        document.querySelector('#play-area').innerHTML += `<div class="die" id="${face}">${arr[face]}</div>`;
        // document.querySelector(`#${face}`).addEventListener('click', function (event) {
        //     die = `<div class="die" id="${face}">${get_dice_roll_value()}</div>`;
        // });
    }
}

function show_dice_v2(arr) {
    for (let face in arr) {
        let die = document.createElement('div');
        die.className = 'die';
        die.id = face;
        die.appendChild(document.createTextNode(arr[face]));
        die.addEventListener('click', function (event) {
            let new_val = get_dice_roll_value();
            die.replaceChild(document.createTextNode(new_val), this.firstChild);
            update_sum()
        });
        document.querySelector('#play-area').appendChild(die)
    }
}

function clear_play_area() {
    let elem = document.querySelector('#play-area');
    while (elem.firstChild) {
        elem.removeChild(elem.firstChild);
    }
}

function clear_display_sum() {
    let elem = document.querySelector("#display_sum");
    elem.innerHTML = '';
}

function update_sum() {
    let nums = document.querySelector('#play-area').childNodes;
    let new_sum = 0;
    for (let divs in nums) {
        if (divs > 0) {
            let is_num = nums[divs].innerText;
            console.log(is_num)
            new_sum += parseInt(is_num);
        }

    }
    show_sum_html(new_sum)
};


function roll() {
    if (document.querySelector('.die')) {
        clear_play_area();
    }

    let num_dice = document.querySelector('#roll-count').value;
    let num_side = document.querySelector('#side-count').value;
    let total = 0;
    let arr = [];
    for (i = 0; i < num_dice; i++) {
        let face = get_dice_roll_value(num_side);
        total += face;
        arr.push(face)
    }
    show_sum_html(total);
    show_dice_v2(arr)
}

document.querySelector('#submit').addEventListener('click', roll);