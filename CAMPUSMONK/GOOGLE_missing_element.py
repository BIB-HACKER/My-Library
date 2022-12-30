# Find missing elements of a range.

# input : 1 14 11 51 15, LOW=50, HIGH=55

# output : 50 52 52 54 55

# size=int(input("="))
# arr=[]

# for i in range(0,size):
#     arr.append(int(input("enter value =>")))
def missing_element(arr,n,low,high):
    
    for i in range(low,high+1):
        if i not in arr:
            print(i,end=" ")


arr=[1,14,11,51,15]
low=50
high=55

n=len(arr)
missing_element(arr,n,low,high)


