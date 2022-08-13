# QUES
# INPUT :-
#           arr1=[9,1,10,1,2,5,99,1,3]
#           arr2=[2,1,9,5]
# OUTPUT :- 
#           arr1=[2, 1, 1, 1, 9, 5, 3, 10, 99]
###########################################################################
n=9
m=4
arr1=[9,1,10,1,2,5,99,1,3]
arr2=[2,1,9,5]
# for i in range(n):
#     arr1.append(int(input("enter number->")))
#     print("*********")
# for i in range(m):
#     arr2.append(int(input("enter number->")))
# print(arr1)
# print(arr2)
dic={}
for j in arr1:
    dic[j]=arr1.count(j)
# print(dic)

list=[]
for i in arr2:
    for j in dic:
        if j==i:
            for k in range(dic[j]):
                list.append(j)
list1=[]
for j in dic:
    if j not in list:
        list1.append(j)
        list1.sort()
for i in list1:
    list.append(i)
#####################
for i in list:
    print(i,end=" ")
# print(list)




