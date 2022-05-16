# import this


# list1 = eval(input("enter first list"))
# list2 = eval(input("enter second list"))
# length1=len(list1)
# length2=len(list2)
# if length1==length2:
#     print("both the list have same number of elements")
# elif length1>length2:
#     print("the list having max no. of elements is list1:-",list1)
# else:
#     print("the list havjing max no. of elements is list2:-",list2)

# #UNION
# list1.extend(list2)
# print(list1)
# list1.sort()
# print(list1)
# unique=[]
# for val in list1:
#     print("A",val)
#     if val not in unique:
#         unique.append(val)
#         print("B",val)
#         print("onno",unique)
# print("unique is =",unique)


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

# A = [9,8,7,6,5]
# B = [5,6,7,8,9]

# A.extend(B)
# print(A)
# A.sort()
# print(A)
# flter=[] # EMPTY list
# for i in A:
#     if i not in flter:
#         flter.append(i) 
# print(flter)

#----------------------------------------------------

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])
#!!!!!!!!!!!!!!!!!!!
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

#---------------------------------------------------

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist =[]
# for i in fruits:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)
# #!!!!!!!!!!!!!!!!!!!
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#############################

# lol = ["a","e","r","o","b","p","z","q"]
# # list=[]
# # for i in lol:
# #     if "a" in i:
# #         list.append(i)
# # print(list)
# print(lol[0:4])
# print(lol[4::-1])
