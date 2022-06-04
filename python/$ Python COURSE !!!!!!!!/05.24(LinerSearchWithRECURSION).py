#in the list Liner search method
def linersearch(list,index,num): #list[23,34]
                                    # [0, 1 ]
    if index==len(list): #list[2]==not found
        return -1
    elif list[index]==num:  # list[0/1]==find
        return index
    else:
        linersearch(list,index+1,num)
#main
size=int(input("how many numbers do you want to enter in a list->"))
list=[]
for i in range(size):
    list.append(int(input("enter numer=")))
#method call
num=int(input("enter a number to search->"))
pos=linersearch(list,0,num)
if pos==-1:
    print(num,"is not found in the list")
else:
    print(num,"is found in list at",pos,"numer index")