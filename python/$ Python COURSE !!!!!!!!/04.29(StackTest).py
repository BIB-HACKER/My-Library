def push(num):
    global stack
    stack.append(num)

def pop():
    global stack
    item=0
    if stack==[]:
        item=-999
    else:
        item=stack.pop()
    return item


#main
stack = []
list=eval(input("create a list"))
for i in list:
    # if i%2==0:
        push(i)
while True:
    item=pop()
    if item==-999:
        break
    else:
        print("POPED vlue is",item)