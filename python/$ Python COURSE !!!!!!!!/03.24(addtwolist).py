#add two list of same size position wise
size = int(input("how many elements ="))
l=eval(input("enter "+str(size)+" integer of 1st list ="))
n=eval(input("enter "+str(size)+" integer of 2st list ="))
m=[]
#ADD
for i in range (0,size):
    m.append(l[i]+n[i])
#DISPLAY
print("the new list is =")
print(m)