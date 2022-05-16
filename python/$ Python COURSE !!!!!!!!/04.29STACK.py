#stack- A linear data structure which follows LIFO(last in first out) policy.
#enter number and then pop -menu driven approch

top=-1
stack=[]
def isempty(stack):
    if stack==[]:
        return True
    else:
        return False

def push(stack,item):
    global top
    top=top+1
    stack.append(item)

def pop(stack):
    global top
    if isempty(stack):
        print("underflow")
    else:
        item=stack.pop()
        print("popped item is =",item)
        top=top-1

def display(stack):
    global top
    if isempty(stack):
        print("stack si empty")
    else:
        print("stack is =")
        for i in range(top,-1,-1):
            print(stack[i])

def peek(stack):
    global top
    if isempty(stack):
        print("stack is empty")
    else:
        print("element at top=",stack[top])

#main
while True:
    print("Menu\n 1. Push\n 2. Pop\n 3.Get the top item\n 4. Display the stack content\n 5.Exit")
    choice=int(input("enter your choice(1-4)"))
    if choice==1:
        item=int(input("enter a number to push"))
        push(stack,item)
    elif choice==2:
        pop(stack)
    elif choice==3:
        peek(stack)
    elif choice==4:
        display(stack)
    else:
        break
