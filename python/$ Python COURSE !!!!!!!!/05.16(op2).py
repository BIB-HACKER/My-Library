def change(alist):
    list=[]
    for i in range(0,len(alist)):
        list.append(alist[i]*2)
    return list


mylist=[1,2,3,4]
change(mylist)
print(mylist)
print(change(mylist))