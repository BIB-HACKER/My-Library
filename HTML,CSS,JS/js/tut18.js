// ***************THIS IS EVENTS PROGRAM****************

console.log('this is tut18');


// let btn = document.getElementById('btn');
// btn.addEventListener('click' , func1);
// btn.addEventListener('mousedown' , func3);
// btn.addEventListener('dblclick' , func2);

// function func1(o) {
//     console.log("thanks" , o);
//     o.preventDefault();
// }

// function func2(o) {
//     console.log("thanks to dblclick" , o);
//     o.preventDefault();
// }

// function func3(o) {
//     console.log("thanks to mousedown" , o);
//     o.preventDefault();
// }

// document.querySelector('.no').addEventListener
// ('mouseenter' , function(){

//     console.log('you entered no.')
// })

// document.querySelector('.no').addEventListener
// ('mouseleave' , function(){

//     console.log('you exit no.')
// })

document.querySelector('.container').addEventListener
    ('mousemove', function (e) {

        console.log(e.offsetX, e.offsetY);
        // document.body.style.backgroundColor = 'red';
        document.body.style.backgroundColor = `rgb(${e.offsetX},${e.offsetX}, ${e.offsetY}, 11)`;
        console.log('you triggered mouse move events');
    });