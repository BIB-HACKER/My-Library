console.log('this is a tut 27')

class employee{
    constructor(name,experience,division)
    {
        this.name = name;
        this.experience = experience;
        this.division = division;
    }

    slogan(){
        return `i am ${this.name} and this company is the best`
    }
    joiningtear(){
        return 2022 - this.experience
    }

    static add(a, b){
        return a + b;
    }
};

let opp = new employee("papon", 6, "engineering")
console.log(opp);
console.log(opp.joiningtear());
console.log(employee.add(43 , 345));

///////////////////////////////////////////////////////////////////////////////

class programmer extends employee{

    constructor(givenname, givenexperince, givendivision, language, github) 
    {
        super(givenname,givenexperince,givendivision);
        this.language = language;
        this.github = github;
    }
    favoritelanguage(){
        if(this.name == 'c++'){
            return 'c++'
        }
        else{
            return 'python'
        }
    }

    static multi (a ,b){
        return a  *b;
    }
};

let ooo = new programmer ("papon",5,"engineering", "c" , "bibhakar404" );
console.log(ooo);
console.log(ooo.favoritelanguage());
console.log(programmer.multi(345, 5));