function get_user_nums() {
    let user_in;
    let nums = [];
    while (user_in != 'done') {
        user_in = prompt('enter a number, or "done" to get average: ').toLowerCase();
        if (user_in === 'done') {
            console.log(get_avg(nums))
        } else {
            nums.push(parseInt(user_in));
            console.log(nums)
        }

    }
}

function get_avg(arr) {
    function add(a, b) {
        return a + b;
    }
    let sum = arr.reduce(add, 0);
    return sum / arr.length
}

get_user_nums();