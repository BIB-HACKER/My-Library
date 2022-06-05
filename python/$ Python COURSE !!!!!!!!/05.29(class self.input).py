# Class Declaration

class Employee: #class name is employee

    def __init__(self): #Constructor
        self.name="bibhakar"  #self.name is the object reference whoo is calling the function
        self.id=0 # self.id is the instance variables
        self.dept="INVENTION"

    def display(self): #INSTANCE METHOD
        print("employee name=",self.name)
        print("employee id=",self.id)
        print("employee dept=",self.dept)
    
    def input(self):
        self.id=int(input("enter employee id->"))

emp=Employee()
emp.input()
emp.display()