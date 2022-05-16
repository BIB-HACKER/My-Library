#Display only the diagonals elements of a N x N sized matrix

#display the matrix
# 1,2,3,4,5
# 5,4,3,2,1
# 9,8,7,6,5
# 5,6,7,8,9
# 2,4,6,8,5

# #display the diagonal
# 1       5
#   4   2 
#     7   
#   6   8 
# 2       5

mat=[] # create a empty lsit
N =0
N = int(input("enter numbers of row"))
for i in range(0,N):
    mat.append([])
    print("for row ",i)
    for j in range(0,N):
        mat[i].append(int(input("enter a number")))
print("original list is :",mat)
#Display the matrix format
for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[i][j],end=" ")
    print()
#Display Diagonals matrix
for i in range(len(mat)):
    for j in range(len(mat)):
        if i==j or i+j==(len(mat)-1):
            print(mat[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()