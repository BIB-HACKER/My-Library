# write a program to take input of a list from user and swap the adjacent element

def swap(list):
    for i in range(0,val,2):
        list[i],list[i+1]=list[i+1],list[i]
    return list

list=eval(input("Create a list =>"))
val=len(list)-1
print(swap(list))

# for i in range(1,11,2):
#     print(i,end=" ")


