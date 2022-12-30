# n=int(input("enter array size ->"))
# arr=[]
# for i in range(0,n):
#     arr.append(int(input("enter number =")))

# mx=arr[0]
# for j in range(0,n):
#     if arr[j]>mx:
#         mx=arr[j]

arr=[11,22,33,44,55]
mx=max(arr)

second_max=-128
for i in range(0,len(arr)):
    if arr[i]!=mx:
        if arr[i]>second_max:
            second_max=arr[i]

print("2nd maximum number is = ",second_max)