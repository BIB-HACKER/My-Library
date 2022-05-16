console.log('we are at tut 6');
const name = 'papon';
const get = 'good night';
// console.log(get +' '+ name);

let html;
htm = "<h1> this is my era </h1>" +
       "<p> this is my pera </p>";

htl = htm.concat('this is ', 'hdefh',' ddDDDDDDDDDDDDDDDDDDDDDDD');
console.log(htl);
// console.log(htl.length);
// console.log(htl.toLowerCase());
// console.log(htl.toUpperCase());
// console.log(htl);

// console.log(htl[0]);
// console.log(htl.indexOf('h1'));
// console.log(htl.lastIndexOf('<'));
// console.log(htl.charAt('1'));
// console.log(htl.endsWith('hdefh'));
// console.log(htl.includes('pera'));
// console.log(htl.substring(0,7));
// console.log(htl.slice(-3));
// console.log(htl.split('>'));
// console.log(htl.replace('this', 'loooool '));

let fruit1 = 'mango\?';
let fruit2 = 'apple';
let myhtl = `Hello ${name}
             <h1> This is "my" Programing and dfefinetly i work hard. </h1>
             <p> you like ${fruit1} and 
             ${fruit2}.`;

document.body.innerHTML = myhtl;