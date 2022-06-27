class Employee:   # BASE CLASS
    def __init__(self,id,name,dept):
        self.name=name
        self.id=id
        self.dept=dept
    
    def display(self):
        print("employee name=",self.name)
        print("employee id=",self.id)
        print("employee department=",self.dept)
         
class Manager(Employee):  # SUBCLASS
    def __init__(self,name,id,dept,grade,noofemployee):
        self.grade=grade
        self.noofemployee=noofemployee
        Employee.__init__(self,id,name,dept)

    def display(self):
        print("grade=",self.grade)
        print("no of employee=",self.noofemployee)
        Employee.display(self)

obj=Manager("bibhakar",5,"inventor","B777",55)
obj.display()