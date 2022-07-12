def push(key):
    global stack
    if employee[key]<85000:
        stack.append(key)
def pop():
    global stack,name
    name+=stack.pop()+" "
    return name  
employee={"Ajay":76000,"Jyothi":150000,"David":89000,"Remya":65000,"Kartika":90000,"Vijay":82000}
stack=[]
for key in employee:
    push(key)
name=""
for i in range(len(stack)):
    name=pop()
print(name)
