#Binary Search
list = eval(input("Enter few numbers in a list in ascending order"))
num=int(input("enter a number to search"))
low = 0
mid = 0
high = len(list)-1

while low<=high:
    mid=(low+high)//2
    if num==list[mid]:
        print("found")
        break
    if num<list[mid]:
        high=mid-1
    else:
        low=mid+1
else:
    print("not found")