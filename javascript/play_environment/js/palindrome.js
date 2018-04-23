let re = /[\W_]/g;
let str = prompt('Give us a word to check if palindrome: ').toLowerCase().replace(re, "");

function check_palindrome(a_str) {

    let a_str_split = a_str.split("")
    let b = a_str_split.reverse();
    b = b.join("")
    return (a_str == b);
}


check_palindrome(str)? console.log('Its a palindrome'): console.log("Its not a palindrome");
