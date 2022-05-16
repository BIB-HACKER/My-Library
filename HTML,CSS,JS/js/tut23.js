console.log('this is a tut23')

let today = new Date();
let otherdate = new Date ('12-30-1999 13:23:42');
console.log(otherdate);

let a;
a = otherdate.getDate();
a = otherdate.getTime();
a = otherdate.getDay();
a = otherdate.getSeconds();
a = otherdate.getHours();
a = otherdate.getMinutes();
console.log(a);

otherdate.setDate(15);
otherdate.setMonth(7);
otherdate.setFullYear(1947);
otherdate.setHours(1);
otherdate.setMinutes(2);
otherdate.setSeconds(3);
console.log(otherdate)



