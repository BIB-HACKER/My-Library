source = eval(input("enter 10 integer in a list"))
list1=[]
for val in range(len(source)-1,-1,-1):
    list1.append(val)        
list1.reverse()
print(source)
print(list1)

 #-----------------------------------------

source = eval(input("enter 10 integer in a list"))
list1=[]
for val in range(0,len(source),+1):
    list1.append(val)        
print(source)
print(list1)