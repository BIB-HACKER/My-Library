const name = 'Bibhakar Paul************';

let html;
   
let mobile = 'asus';
let pc =  'Lenevo';
// let oo = '<link rel="stylesheet" href="LINK.css">';
let ht = '<a href="http://facebook.com" class="me" id="that" ><b> bibHACKER</b></a>'

let hm = '<a href="form.html"><big>link</big></a> '

let myhtml = `hello ${name}
            <h1><b><i> NOW THIS IS MY LOCAL AREA AND BUILD MY OWN POWER HOUSE </i></b></h1>
            <p> your mobile phone is ${mobile} </p>
            <p> you used ${pc} pc.</p>
            <p>${ht}</p>
            <p>${hm}</p>`;

document.body.innerHTML = myhtml;