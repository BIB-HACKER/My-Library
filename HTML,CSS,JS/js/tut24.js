console.log('this is tut24')

// object leteral for creating object
let car = {
    name: 'Range rover difender',
    topspeed: 100,
    run: function () {
        console.log("car is so hard and sexy");
    }
}
// console.log(car)


function GeneralCar(givename, givenspeed) {
    this.name = givename;
    this.speed = givenspeed;


    this.run = function () {
        console.log(`${this.name} is running, but this car slower ${500 - this.speed} km/h then roket`);
    }
}
car = new GeneralCar('Rangerover', 220);
console.log(car);