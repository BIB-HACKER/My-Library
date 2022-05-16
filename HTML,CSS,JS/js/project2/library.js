console.log('this is library js')

// constructor function
function Book(name, author, type) {
    this.name = name;
    this.author = author;
    this.type = type;
}

//display function
function Display() {

}

//and method to display prototype
Display.prototype.add = function (book) {
    console.log("Adding to UI");
    tableBody = document.getElementById('tableBody');
    let uiString = `<tr>
                         <td>${book.name}</td>
                         <td>${book.author}</td>
                         <td>${book.type}</td>
                    </td>`;
    tableBody.innerHTML += uiString;
}

//Implement the clear function
Display.prototype.clear = function () {
    let libraryForm = document.getElementById('libraryForm');
    libraryForm.reset();
}

//Implement the validate function
Display.prototype.validate = function (book) {
    if (book.name.length < 2 || book.author.length < 2) {
        return false
    }
    else {
        return true;
    }
}
Display.prototype.show = function (type, displayMessage) {
    let message = document.getElementById('message');
    message.innerHTML = `<div class = "alert alert-${type} alert-dismissible fade show" role="alert">
                            <strong>messge:</strong> ${displayMessage}
                            <button type="button" class="close" date-dismiss="alert" aria-lable="Close">
                            <span aria-hidden="true">x</span>
                            </button>
                         </div>`;
    setTimeout(function () {
        message.innerHTML = ''
    }, 4000);

}


//add submit event listener to form
let libraryForm = document.getElementById('libraryForm');
libraryForm.addEventListener('submit', libraryFormSubmit);


function libraryFormSubmit(e) {
    console.log('you have submitted library form');
    let name = document.getElementById('bookName').value;
    let author = document.getElementById('author').value;

    // Mobilephonerepairing, programming, EthicalHacking;
    let type;

    let mobilephonerepairing = document.getElementById('mobilephonerepairing');
    let programming = document.getElementById('programming');
    let EthicalHacking = document.getElementById('EthicalHacking');

    if (mobilephonerepairing.checked) {
        type = mobilephonerepairing.value;
    }
    else if (programming.checked) {
        type = programming.value;
    }
    else if (EthicalHacking.checked) {
        type = EthicalHacking.value;
    }

    let book = new Book(name, author, type);
    console.log(book);

    let display = new Display();

    if (display.validate(book)) {
        display.add(book)
        display.clear();
        display.show('success', 'your book has been successfully added')
    }
    else {
        //show error to the user
        display.show('danger', 'sorry you cannot add this book');
    }

    e.preventDefault();
}
