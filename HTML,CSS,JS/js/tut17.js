// JS EVENT CODE-->

console.log('this is tut 17');

document.getElementById("heading").addEventListener("mouseover", function (e) {
    let variable;
    console.log('you have click the events');
    variable = e.target;
    variable = e.target.className;
    variable = e.target.classList;

    variable = Array.from(e.target.classList);

    // variable = e.target.id;
    variable = e.offsetX;
    variable = e.offsetY;
    variable = e.clientX;
    variable = e.clientY;
    console.log(variable);
    // console.log(e);
    // location.href = '//google.com';
});


