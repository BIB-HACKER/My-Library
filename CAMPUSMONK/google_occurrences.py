# find k number of most occurrences/frequence in the given arrau.

# input : 3 1 4 4 5 2 6 1, k = 2
# output : 4 1

arr=[3,1,4,4,5,2,6,1]
k=2
n=len(arr)
list=[]
for i in range(0,n):
    if arr.count(arr[i])==k:
        if arr[i] not in list:
            list.append(arr[i])
    
for i in (list[-1::-(len(list)-1)]):
    print(i,end=" ")

