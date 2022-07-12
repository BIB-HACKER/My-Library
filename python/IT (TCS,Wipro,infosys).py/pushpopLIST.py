def push(num):
    global stack
    if num%5==0 and num%3==0:
        stack.append(num)
def pop():
    global stack
    if stack!=[]:
        print(stack.pop(),end=" ") 
        return 0
    else:
        return None  
stack=[]
# L=eval(int(input("enter 8 time number=")))
L=[5,15,21,30,45,50,60,75]
for num in L:
    push(num)    
while True:
    if pop()==None:
        break