# (1,"bibhakar","6297535683"),(2,"malay","9865657656"),(3,"swaraj","9776876675")

def push(tuple):
    global namestack
    global phonebook
    if tuple[0]<=10:
        namestack.append(tuple[1])
        phonebook.append(tuple[2])

def pop():
    if namestack!=[]:
        print(namestack.pop()," ",phonebook.pop())
        return 0
    else:
        return None

students=[]
for i in range(3):
    record=eval(input("enter id,name,phone no. in a tuple= "))
    students.append(record)

namestack=[]
phonebook=[]
for tuple in students:
    push(tuple)

# print(namestack)
# print(phonebook)
while True:
    if pop()==None:
        break



