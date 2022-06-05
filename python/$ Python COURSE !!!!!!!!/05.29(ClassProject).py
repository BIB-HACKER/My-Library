class Project:

    def __init__(self,id,title,cost,hours):
        self.id=id
        self.title=title
        self.cost=cost
        self.hours=hours

    def get_id(self):   #value show
        return self.id
    def get_title(self):
        return self.title
    def get_cost(self):
        return self.cost
    def get_hours(self):
        return self.hours

    def set_id(self,id):   # value update
        self.id=id
    def set_title(self,title):
        self.title=title
    def set_cost(self,cost):
        self.cost=cost
    def set_hours(self,hours):
        self.hours=hours

    # def display(self):
    #     print("project id= ",self.id)
    #     print("project title name= ",self.title)
    #     print("Total project cost= ",self.cost)
    #     print("Total project making hours= ",self.hours)


Pj1=Project(11,'AVTAR1',22000,48)
Pj2=Project(21,'AVTAR2',22000,58)
Pj3=Project(43,'AVTAR3',22000,68)
Pj4=Project(22,'AVTAR4',22000,78)

# Pj1.display()
# Pj2.display()
# Pj3.display()
# Pj4.display()

# value display
print(Pj1.get_id(),end=" ")
print(Pj1.get_title(),end=" ")
print(Pj1.get_cost(),end=" ")
print(Pj1.get_hours())
print(Pj2.get_id(),end=" ")
print(Pj2.get_title(),end=" ")
print(Pj2.get_cost(),end=" ")
print(Pj2.get_hours())
print(Pj3.get_id(),end=" ")
print(Pj3.get_title(),end=" ")
print(Pj3.get_cost(),end=" ")
print(Pj3.get_hours())
print(Pj4.get_id(),end=" ")
print(Pj4.get_title(),end=" ")
print(Pj4.get_cost(),end=" ")
print(Pj4.get_hours(),end=" ")

# After value edit
Pj1.set_cost(Pj1.get_cost()+Pj1.get_cost()*.05)
Pj1.set_hours(Pj1.get_hours()-5)
Pj2.set_cost(Pj2.get_cost()+Pj2.get_cost()*.05)
Pj2.set_hours(Pj2.get_hours()-5)
Pj3.set_cost(Pj3.get_cost()+Pj3.get_cost()*.05)
Pj3.set_hours(Pj3.get_hours()-5)
Pj4.set_cost(Pj4.get_cost()+Pj4.get_cost()*.05)
Pj4.set_hours(Pj4.get_hours()-5)
print()
print()
print(Pj1.get_id(),end=" ")
print(Pj1.get_title(),end=" ")
print(Pj1.get_cost(),end=" ")
print(Pj1.get_hours())
print(Pj2.get_id(),end=" ")
print(Pj2.get_title(),end=" ")
print(Pj2.get_cost(),end=" ")
print(Pj2.get_hours())
print(Pj3.get_id(),end=" ")
print(Pj3.get_title(),end=" ")
print(Pj3.get_cost(),end=" ")
print(Pj3.get_hours())
print(Pj4.get_id(),end=" ")
print(Pj4.get_title(),end=" ")
print(Pj4.get_cost(),end=" ")
print(Pj4.get_hours(),end=" ")