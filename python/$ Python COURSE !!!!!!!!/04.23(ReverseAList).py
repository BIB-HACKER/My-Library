def reverseALlist(list):
    first=0
    last=len(list)-1
    while first<last:
        list[first],list[last]=list[last],list[first]
        first+=1
        last-=1

#main
n=int(input("enter number of element of the list"))
list=[]
for count in range(0,n):
    num=int(input("enter a number"))
    list.append(num)
print("the list is=",list)
reverseALlist(list)#method call
print("the reverse list is= ",list)