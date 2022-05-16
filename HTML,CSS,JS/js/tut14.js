// THIS IS DOM SELECTOR---> 

/* element selector ->
1. single element selector
2. multiple element selector*/

console.log('this is tut14');

a = document.all
// console.log(a)

// 1.Single element selector
let element = document.getElementById('myfirst');
// element = element.classname;
// element = element.childNodes;
// element = element.parentNode;
element.style.color = 'Red';
element.innerText = 'hii im bibhakar';
element.innerHTML = '<b>bibhakar';
// console.log(element.innerText);

let sel = document.querySelector('#myfirst');
// pound(#) = ID
 sel = document.querySelector('.child');
 // dot(.) = class
 sel = document.querySelector('h1');
 sel = document.querySelector('div');
 sel.style.color = 'green';
//  console.log(sel);

//2. Multi element selector
let ell = document.getElementsByClassName('child');
ell = document.getElementsByClassName('container');
ell = document.getElementsByTagName('div');
console.log(ell);

for (let index = 0; index < ell.length; index++) {
    const element = ell[index];
    console.log(element);
    element.style.color = 'blue';
}

// Array.from(ell).forEach(element=> {
//     console.log(element);
//     element.style.color = 'blue';
// });




