console.log('this is tut 26')

const proto = {
    slogan: function () {
        return `this companty is the best`;
    },
    changeName: function (newname) {
        this.name = newname
    }
}
let papon = Object.create(proto);
papon.name = "papon";
papon.role = "programer";
papon.changeName("bibhakar");
// console.log(papon)

let papon1 = Object.create(proto, {
    name: { value: "bobobob", writable: true },
    role: { value: "propopo" },
});
// papon1.changeName("papon2")
// console.log(papon1)



//employee constructor

function employee(name, salary, experience) {
    this.name = name;
    this.salary = salary;
    this.experience = experience;
}

//slogan
employee.prototype.slogan = function () {
    return `this company is the best, ${this.name}, ${this.salary}, ${this.experience}`;
}
// create obj is a object
let obj = new employee("papon", 34535, 7);
// console.log(obj.slogan())

///////////////////////////////////////
function programer(name, salary, experience) {
    this.name = name;
    this.salary = salary;
    this.experience = experience;
}

let output = new programer("Bibhakar", 45555, 4);
// console.log(output);
//////////////////////////////////////


// pro set constructor 
function pro(name, salary, experience, language) {
    programer.call(this, name, salary, experience);
    this.language = language;
}

programer.prototype = Object.create(employee.prototype);

//manualy set the constructor
programer.prototype.constructor = pro;

//set the object
let answer = new pro("papon", 355672, 6, "python");
console.log(answer);


