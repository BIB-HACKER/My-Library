#BublleSort
N = int(input("how many numbers do you input in the list :"))
list = eval(input("enter numbers in the list"))
i = 1
N = len(list)
while i<N:
    flag = 0
    j = 0
    while j<N-i-1:
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            flag=0
        j+=1
    if flag==1:
        break
    i+=1
print("Sorted list is")
print(list)