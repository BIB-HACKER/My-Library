# list1 = eval(input("enter your list numbers"))
# list2=[]
# list2=list1
# list2.reverse()
# print(list2) #100% NOT TRUE

#---------------------------------------------

source = eval(input("enter 10 integer in a list"))
list1=[]
for val in source:
    list1.append(val)        
list1.reverse()
print(source)
print(list1)

 #-----------------------------------------

source = eval(input("enter 10 integer in a list"))
list1=[]
for val in range(len(source)-1,-1,-1):
    list1.append(source[val])        
# list1.reverse()
print(source)
print(list1)


