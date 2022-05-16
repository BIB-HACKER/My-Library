/********************************this is a localstorage & sessionstorage tut20**************************/

console.log('this is a tut20');
let impArray = ['cricket', 'footbal', 'chess'];

localStorage.setItem('Name', 'papon');
localStorage.setItem('Name2', 'pap');
// localStorage.setItem('game', JSON.stringify(ipmArray));

// localStorage.clear(); /* full storage clear this command(localstorage.clear)/*

// localStorage.removeItem('Name')
// localStorage.removeItem('Name2')

let oooo = localStorage.getItem('Name2')
console.log(oooo);

let tumiamar = localStorage.getItem('Name');
// tumiamar = JSON.parsef(localStorage.getItem('game'));
console.log(tumiamar);

sessionStorage.setItem('sessionName', 'spapon');
// sessionStorage.clear();