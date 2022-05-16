// HOW TO CREATE A Element

console.log('welcome to tut 16');

let element = document.createElement('li');
let text = document.createTextNode('i am a text no');
element.appendChild(text)
// add a class element to the li element
element.className = 'child5'
element.id = 'createli'
element.setAttribute('title', 'my life')
// element.innerText = 'bibHACKER'
// element.innerHTML = 'bibHACKER'

let ul = document.querySelector('ul.this');
ul.appendChild(element);

// console.log(ul);
// console.log(element);

// let elem2 = document.createElement('h3');
// elem2.id = 'elem2';
// elem2.className = 'elem2';
// let tnode = document.createTextNode('this is a created node for elem2');
// elem2.appendChild(tnode);

// element.replaceWith(elem2);
// let myul = document.getElementById('myul');
// myul.replaceChild(element, document.getElementById('fui'));
// myul.removeChild(document.getElementById('lui'));
// let pr = elem2.hasAttribute('href');
// elem2.removeAttribute('id');
// elem2.setAttribute('title', 'myelem2title')
// console.log(elem2, pr);

let me = document.createElement('h1');
tnode = document.createTextNode('go to codewithharry');
// me.text = 'go link'
// me.setAttribute('href', 'http//www.google.com')
me.appendChild(tnode);
element.replaceWith(me)
// let ul = document.querySelector('ul.http//www.google.com')
// console.log(me);

