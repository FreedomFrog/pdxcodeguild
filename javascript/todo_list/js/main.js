let num_entry = 0;

// let source;
//
//   function isbefore(a, b) {
//     if (a.parentNode == b.parentNode) {
//       for (let cur = a; cur; cur = cur.previousSibling) {
//         if (cur === b) {
//           return true;
//         }
//       }
//     }
//     return false;
//   }
//
//   function dragenter(e) {
//     if (isbefore(source, e.target)) {
//       e.target.parentNode.insertBefore(source, e.target);
//     }
//     else {
//       e.target.parentNode.insertBefore(source, e.target.nextSibling);
//     }
//   }
//
//   function dragstart(e) {
//     source = e.target;
//     e.dataTransfer.effectAllowed = 'move';
//   }

function addToList() {
    let list = document.getElementById('list');
    let in_text = document.querySelector("#newItem").value;
    let entry = document.createElement('li');
    entry.id = num_entry.toString();
    // entry.draggable = true;
    // entry.ondragenter = dragenter(event);
    // entry.ondragstart = dragstart(event);
    num_entry++;
    // let checkbox = document.createElement('input');
    let remove_btn = document.createElement('BUTTON');
    remove_btn.id = in_text + '-rem';
    remove_btn.addEventListener("click", function () {
        document.getElementById(entry.id).style.display = "none"
    });
    let remove_btn_text = document.createTextNode("Remove");
    remove_btn.appendChild(remove_btn_text);
    let complete_btn = document.createElement("BUTTON");
    complete_btn.id = in_text + '-comp';
    complete_btn.addEventListener("click", function () {
        document.getElementById(entry.id).style.display = "none";
        let comp_list = document.getElementById('completed-list');
        let comp_entry = document.createElement('li');
        comp_entry.appendChild(document.createTextNode(in_text));
        comp_list.append(comp_entry);
    });
    let complete_btn_text = document.createTextNode("Complete");
    complete_btn.appendChild(complete_btn_text);

    // checkbox.type = "checkbox";
    // checkbox.name = "name";
    // checkbox.value = "value";
    // checkbox.id = "id";
    //
    // entry.appendChild(checkbox);
    entry.appendChild(document.createTextNode(in_text + '\n'));
    entry.appendChild(remove_btn);
    entry.appendChild(complete_btn);
    list.appendChild(entry);
    document.querySelector('#newItem').value = '';

}

document.getElementById('enter').addEventListener('click', addToList);



