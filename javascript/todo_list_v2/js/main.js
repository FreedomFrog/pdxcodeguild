function addItem () {
    let item_text = document.querySelector('#newItem').value;
    let todo_list = document.querySelector('#list');
    let todo_item = document.createElement('li');
    todo_item.innerText = item_text;
    let rem_button = remove_button();
    let com_button = complete_button();
    todo_item.appendChild(rem_button);
    todo_item.appendChild(com_button);
    todo_list.appendChild(todo_item)


}

function remove_button () {
    let rem_button = document.createElement('BUTTON');
    let item_text = document.createTextNode('Remove');
    rem_button.appendChild(item_text);
    rem_button.addEventListener('click', remove_from_list);
    return rem_button
}

function remove_from_list (event) {
    this.parentElement.remove();
}

function complete_button () {
    let com_button = document.createElement('BUTTON');
    let item_text = document.createTextNode('Mark Complete');
    com_button.appendChild(item_text);
    com_button.addEventListener('click', move_from_list);
    return com_button
}

function move_from_list (event) {
    let the_inner_html = this.parentNode.;
    //the_inner_html = document.createTextNode(the_inner_html)
    console.log(the_inner_html);
    let complete_item = document.createElement('li');
    let complete_list = document.querySelector('#completed-list');
    complete_item.appendChild(the_inner_html);
    complete_list.appendChild(complete_item);

}

document.querySelector('#enter').addEventListener('click', addItem)
