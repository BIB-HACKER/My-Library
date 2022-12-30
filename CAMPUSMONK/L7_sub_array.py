n=int(input("enter array size ="))
arr=[]
for i in range(0,n):
    arr.append(int(input("enter value ->")))

target=int(input("enter target value =>"))
p=1
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum==target:
            print("yes")
            p=0
            break
if p==1:
   print("Not found")