[[1,2,3,4,5],[5,6,7,9,8],[9,8,7,6,5]]
list=eval(input("create a sublist :"))
print("length of list is ",len(list))
for i in range(len(list)):
    print("sublist no. #",i+1)
    print("sum of this sublist ",sum(list[i]))
    print("maximum number this sublist ",max(list[i]))
    print("minimum number this sublist ",min(list[i]))
#enter the sublist nuber and enter a value. append the value in the sublist
sublist=int(input("enter sublist number :"))
value=int(input("enter the value :"))
if sublist>len(list):
    list.append([])
    list[len(list)-1].append(value)
else:
    for i in range(len(list)):
        if i+1==sublist:
           list[i].append(value)
print(list)
print("The Matrix is :")
for row in range(len(list)):
    for col in range(len(list[row])):
        print(list[row][col],end=" ")
    print()

