// type conversion and type coercion
console.log('welcome to tut5')
let myvar;
myvar = String (56);
console.log(myvar, (typeof myvar));
let bool = String (true);
console.log( bool ,(typeof bool));
let date = String(new Date());
console.log( date ,(typeof date));
let arr = String([4,6,67,8,88,]);
console.log( arr.length ,(typeof arr));

let i = new Date();
console.log(i.toString());

let o = 64;
console.log(o.toString());

let stri =Number("456767");
stri =Number("45de6767");
stri =Number(true);
stri =(false);
stri =Number([5,5,5,5,556,77]);
console.log(stri ,(typeof stri));

// let number =Number("8767.987");
let number =parseFloat("8767.987");
console.log(number.toFixed(5), (typeof number));

// type coercion-->

// let mystring = Number("567");
// let mynumber = 46;
let mystring = "tui";
let mynumber = "ami";
console.log(mystring + mynumber);


