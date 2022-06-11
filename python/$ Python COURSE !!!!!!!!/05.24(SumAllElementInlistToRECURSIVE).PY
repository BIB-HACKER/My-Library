from typing import List



def getsum(list,n):
    if n==0:
        return 0
    else:
        return list[n-1] + getsum(list,n-1)
# list=[1,2,3,4,5]
# getsum(list, 5)
# return list[4] + getsum(list,4)
# return list[4] + list[3] + getsum(list,3)
# return list[4] + list[3] + list[2] + getsum(list,2)
# return list[4] + list[3] + list[2] + list[1] + getsum(list,1)
# return list[4] + list[3] + list[2] + list[1] + list[0] + getsum(list,0)
# return
# return list[4] + list[3] + list[2] + list[1] + list[0] + 0
# return list[4] + list[3] + list[2] + list[1] + 1 + 0
# return list[4] + list[3] + list[2] + 2 + 1
# return list[4] + list[3] + 3 + 3
# return list[4] + 4 + 6
# return 5 + 10
# return 15


n=int(input("'How many numbers to add in the list->"))
list=[]
for count in range(n):
    list.append(int(input("enter a number= ")))
print(list, n)
sum=getsum(list,n)

print("Sum of the list elements is: ",sum)