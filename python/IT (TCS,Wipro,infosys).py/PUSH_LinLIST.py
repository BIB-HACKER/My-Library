def PUSH(val):
    global list
    list.append(val)

def pop():
    even=0
    if list==[]:
        even=-1
    else:
        even=list.pop()
    return even
#main
L=[]
for i in range(1,1001):
    L.append(i)

list=[]
for val in L:
    if val%2==0:
        PUSH(val)
# print(list)
while True:
    even=pop()
    if even==-1:
        break
    else:
        print(even,end=" ")
        



