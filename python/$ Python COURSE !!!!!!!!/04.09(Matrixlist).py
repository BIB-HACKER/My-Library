[[1,2,3,4,5],[5,6,7,9,8],[9,8,7,6,5],[9,8,7,6,5]]
list=eval(input("enter 16 digit in 4 x 4 matrix :"))
rowsum=0
allsum=0
print("The Matrix is :")
for row in range(len(list)):
    for col in range(len(list[row])):
        print(list[row][col],end=" ")
    print()
for row in range(len(list)):
    rowsum= sum(list[row])
    allsum +=rowsum
    print("Row no.",row+1)
    print("sum of the all elements is :",rowsum)
print("total 16 digits matrix numbers is :",allsum)
