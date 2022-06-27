
a = 11
b = 21.5
c = "malay python na kore only HTML/CSS kore"

def fixing(x,y):
    return x*y

class Programmer:
    company='Microsoft'

    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        p = (f"the name of the programmer is {self.name} and the product is {self.product} and her company is {self.company}")
        return p


