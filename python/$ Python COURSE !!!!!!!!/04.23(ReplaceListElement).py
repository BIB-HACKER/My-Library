# Replace each element of a list by adding a specific number using user-defined method-
# User-defined function to update a list
def replaceAlist(list,num):
    index=0
    while index<len(list):
        list[index]=list[index]+num
        index+=1   

#main
n=int(input("enter number of element fo the list"))
list=[]
for i in range(0,n):
    num=int(input("enter a number of elements"))
    list.append(num)
#outside the for loop
num=int(input("enter a number to update list elements"))
print("the list is= ",list)
replaceAlist(list,num)#method call
print("the replace list is= ",list)