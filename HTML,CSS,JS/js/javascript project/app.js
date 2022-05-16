console.log('welcome to magic notes, this is app.js');
showNotes();

// if user adds a note. add it to the localstorage
let addBtn = document.getElementById('addBtn');
addBtn.addEventListener("click", function (e) {

    let addTxt = document.getElementById("addTxt");
    let addTitle = document.getElementById("addTitle");
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesOBj = [];
    }
    else {
        notesOBj = JSON.parse(notes);
    }
    let myobj = {
        title: addTitle.value,
        text: addTxt.value
    }
    notesOBj.push(myobj);
    localStorage.setItem("notes", JSON.stringify(notesOBj));
    addTitle.value = "";
    addTxt.value = "";
    // console.log(notesOBj);
    showNotes();
})

//Function to show element form localstorage
function showNotes() {
    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesOBj = [];
    }
    else {
        notesOBj = JSON.parse(notes);
    }
    let html = "";
    notesOBj.forEach(function (element, index) {
        html += `
        <div class="notecard my-2 mx-2 card" style="width: 18rem;"> 
              <div class="card-body">
                <h5 class="card-title">${element.title}</h5>
                <p class="card-text">${element.text}</p>
                <button id="${index}" onclick="deleteNote(this.id)" class="btn btn-primary">Delete Notes</button>
              </div>
            </div>`;

    });
    let notesElm = document.getElementById('notes');
    if (notesOBj.length != 0) {
        notesElm.innerHTML = html;
    }
    else {
        notesElm.innerHTML = 'Noting to show! "add a note" section above to add notes.';
    }
}


//Function to delete a note
function deleteNote(index) {
    // console.log('I am deleting', index);

    let notes = localStorage.getItem("notes");
    if (notes == null) {
        notesOBj = [];
    }
    else {
        notesOBj = JSON.parse(notes);
    }

    notesOBj.splice(index, 1);
    localStorage.setItem("notes", JSON.stringify(notesOBj));
    showNotes();
}


// Searching
let search = document.getElementById('searchTxt');
search.addEventListener("input", function () {

    let inputval = search.value.toLowerCase();
    // console.log('Input event fired!', inputval);
    let notecards = document.getElementsByClassName('notecard');
    Array.from(notecards).forEach(function (element) {
        let cardTxt = element.getElementsByTagName("p")[0].innerText;
        if (cardTxt.includes(inputval)) {
            element.style.display = "block";
        }
        else {
            element.style.display = "none";
        }

        // console.log(cardTxt);

    })
});

/* 
Further Feature:
1. add title
2. mark a note as important
3. separate note by user
4. sync and host to web server
*/
