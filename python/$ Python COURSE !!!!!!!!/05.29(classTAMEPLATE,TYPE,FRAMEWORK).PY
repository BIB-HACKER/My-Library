# Class Declaration

class Employee: #class name is employee

    def __init__(self,name,id,dept): #Constructor
        self.na=name  #self.name is the object reference whoo is calling the function
        self.i=id # self.id is the instance variables
        self.de=dept

    def display(self): #INSTANCE METHOD
        print("employee name=",self.na)
        print("employee id=",self.i)
        print("employee dept=",self.de)

# emp1=Employee("bibhakar",22,"IT")  #OBJECT CREATION
# emp1.display()  #calling of instance method

#List Of Object
# listofemployee=[]
# listofemployee.append(Employee("bibhakar",22,"Inventor"))
# listofemployee.append(Employee("malay",22,"bekar"))
# for obj in listofemployee:
Employee("bibhakar",22,"Inventor").display()