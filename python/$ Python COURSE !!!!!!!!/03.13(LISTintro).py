# # List collection of values can be store in memory.
# # Their reference are stored in a location called list.list is muteable(cangable in nature)

# mylist=[1,3,5,7,9,11]
# print(mylist[0])
# print(mylist[-1])
# print("the list is :-",mylist)
# print("the list is :-")
# for val in range(len(mylist)):
#     print(val,end=" ")
# print()
# for val in mylist:
#     print(val,end=" ")
# print()
# print("accesing list elements through index no")
# for index in range(0,len(mylist)):
#     # print(mylist)
#     print(mylist[index])
#     print([index])
#     break

# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

list=eval(input("enter 5 number"))
for i in range(len(list)-1,-1,-1):
    print(list[i],end=" ")

# list=eval(input("enter 5 number"))
# for i in range(-1,-len(list)-1,-1):
#     print(list[i],end=" ")

# list=eval(input("enter number"))
# n=[]
# for i in range(len(list)-1,-1,-1):
#     n.append(list[i])
# print(n)



