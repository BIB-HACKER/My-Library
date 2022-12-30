# You are given an array A of size N.
# The cost of an element at the i^th index of the aray is given as I "A[i]"

# write a program to find the total cost of the array.

n=int(input("size of array ->"))
a=[]
for i in range(0,n):
    a.append(int(input("enter item =")))

# val=1
sum=0
# for i in a:
#     sum+=val*i
#     val+=1
for i in range(1,n+1):
    sum+=((a[i-1])*i)

print(sum)