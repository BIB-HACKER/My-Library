n=int(input("enter length of list -->"))
arr=[]
# input -> number of element
for i in range(0,n):
    arr.append(int(input("enter numer ->")))

# output -> min element from the array.
mn=arr[0]
for i in range(0,n):
    if arr[i]<mn:
        mn=arr[i]

print("small number in array =",mn)
##########################################################
n=int(input("enter length of list -->"))
arr=[]
# input -> number of element
for i in range(0,n):
    arr.append(int(input("enter numer ->")))

# output -> max element from the array.
mx=arr[0]
for i in range(0,n):
    if arr[i]>mx:
        mx=arr[i]

print("small number in array =",mn)