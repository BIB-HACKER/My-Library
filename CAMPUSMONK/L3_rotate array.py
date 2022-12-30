#[3,2,1,0]---input
#[0,3,2,1]

n=int(input("enter list size1 ->"))
arr=[]
for i in range(0,n):
    arr.append(input("enter value ->"))
print(' '.join(arr))
last=arr[n-1]
for i in range(len(arr)-1, 0, -1):
    arr[i]=arr[i-1]
arr[0]=last
# for i in arr:
#     print(i,end=" ")
print(' '.join(arr))
