#find the frequency of a number in a list of a numbers
#[3,5,7,8,5,3,3,97,6]
#find the line frequency of 5

from itertools import count


list=[] # creates a empty list
n = int(input("how many numbers in a lis"))
#input to the list
for x in range(1,n+1):
    val=int(input("what the numbers"))
    list.append(val)
#end of the loop
print("this is a list =",list)
search = int(input("enter a number to search -"))
count = 0
# searching
for maching in range(0,len(list)#n
):
    if list[maching]==search:
        count+=1
#number = list.count(search)
#display
if count==0:
    print(search,"is not found in the list")
else:
    print(search,"has frequency",count,"in the list")

#--------------------------------------


    

