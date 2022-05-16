console.log('this is tut 25')

// let obj = {
//     name: "BIBHAKAKR",
//     course: "java script",
//     address: "peace",
// }

// console.log(obj)

function obj(givenname){
//this is a constractor(obj)    
    this.name = givenname
}

obj.prototype.getName = function (){
    return this.name;
}

obj.prototype.setName = function (newname){
    this.name = newname;
}

let o = new obj("papon")
console.log(o);