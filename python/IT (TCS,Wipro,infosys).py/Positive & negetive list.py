list = eval(input("create a list :"))
list.sort()
list1 = []
list2 = []
for i in list:
     if i>0:
         list1.append(i)
     else:
         list2.append(i)
print("LIST is A")
print(list)
print("Positive list is :")
print(list1)
print("Negetive list is :")
print(list2)