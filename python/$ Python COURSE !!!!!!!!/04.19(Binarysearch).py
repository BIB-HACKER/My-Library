#Binary search in a sorted list
list=[]
#this meyhod returns the index of the number if found otherwise returns -1
#this method follow binary search technique
def isfoundbinarysearch(num):
    low=0
    high=len(list)-1
    mid=0
    while low<=high: #0<=5
        mid=(low+high)//2# mid index search
        if list[mid]==num:
            return mid
        if list[mid]>num:
            high=mid-1
        else:
            low=mid+1
    return -1 

def search():
    num=int(input("enter a number to search"))
    pos=isfoundbinarysearch(num)
    if pos != -1:
        print("number found at",pos+1, "position")
    else:
        print("number not found")

def getinput():
    n=int(input("how may number you add in a list"))
    print("input numbers in ascending order")
    for i in range(0,n):
        list.append(int(input("enter a number")))

getinput()
search()
