console.log('welcome to tut15');

let ccc = document.querySelector('.no');
// console.log(ccc);
ccc = document.querySelector('.container');
// console.log(ccc.childNodes);
// console.log(ccc.children);

let nodename = ccc.childNodes[0].nodeName;
// console.log(nodename);
let nodeType = ccc.childNodes[8].nodeType;
// console.log(nodeType);

// NODE TYPE-->
// 1.Element
// 2.Attribute
// 3.Text Node
// 8.Comment
// 9.document
// 10.dotype

let container = document.querySelector('div.container');
// console.log(container.children[1].children[0].children);

// console.log(container.firstChild);
// console.log(container.firstElementChild)
// console.log(container.lastElementChild);
// console.log(container.firstElementChild);
// console.log(container.firstChild);
console.log(container.firstElementChild.parentNode);
console.log(container.firstElementChild.nextSibling);
console.log(container.firstElementChild.nextElementSibling);
console.log(container.firstElementChild.nextElementSibling.nextElementSibling);
console.log(container.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling);