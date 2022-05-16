# #       [   0     ,    1    ,   2     ,   3    ]
# from re import T


# matrix=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[6,5,4,3]]
# #      [[0,1,2,3],[0,1,2,3],[0,1,2,3,],[0,1,2,3]]
# row=len(matrix)#4
# col=len(matrix[0])#4
# print("the matrix is =")
# for i in range(0,row):
#     for j in range(0,col):
#         print(matrix[i][j],end=" ")
#     print()
# #identify and display boundary elements
# print("the boundary elements are =")
# for i in range(0,row):
#     for j in range(0,col):
#         if i==0 or j==0 or i==row-1 or j==col-1:
#             print(matrix[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #display sum of bundary elements and also display the height and lowest boundary elements
# # identify and display only the primary and secondary diagonal elements
# print("the diagonal elements are=")
# for i in range(0,row):
#     for j in range(0,col):
#         if i==j or i+j==(len(matrix)-1):
#             print(matrix[i][j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()

########################################################

# matrix=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[6,5,4,3]]
# row=len(matrix)
# col=len(matrix[0])

def getmatrix():
    print("the matrix is =")
    for i in range(0,row):
        for j in range(0,col):
            print(matrix[i][j],end=" ")
        print()

def getboundary():
#identify and display boundary elements
    print("the boundary elements are =")
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or j==0 or i==row-1 or j==col-1:
                print(matrix[i][j],end=" ")
            else:
                print(" ",end=" ")
        print()

def getdiagonal():
# #display sum of bundary elements and also display the height and lowest boundary elements
#identify and display only the primary and secondary diagonal elements
    print("the diagonal elements are=")
    for i in range(0,row):
        for j in range(0,col):
            if i==j or i+j==(len(matrix)-1):
                print(matrix[i][j],end=" ")
            else:
                print(" ",end=" ")
        print()

matrix=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[6,5,4,3]]
row=len(matrix)
col=len(matrix[0])
getmatrix()
getboundary()
getdiagonal()

# ################################################


# def getmatrix():
#     print("the matrix is =")
#     for i in range(0,row):
#         for j in range(0,col):
#             print(matrix[i][j],end=" ")
#         print()

# def getboundary():
# #identify and display boundary elements
#     print("the boundary elements are =")
#     for i in range(0,row):
#         for j in range(0,col):
#             if i==0 or j==0 or i==row-1 or j==col-1:
#                 print(matrix[i][j],end=" ")
#             else:
#                 print(" ",end=" ")
#         print()

# def getdiagonal(n):
# # #display sum of bundary elements and also display the height and lowest boundary elements
# #identify and display only the primary and secondary diagonal elements
#     print("the diagonal elements are=")
#     for i in range(0,row):
#         for j in range(0,col):
#             if i==j or i+j==(len(matrix)-1):
#                 return (matrix[i][j])
#             else:
#                 return (" ")
#         print()

# matrix=[[1,2,3,4],[4,5,6,7],[7,8,9,1],[6,5,4,3]]
# row=len(matrix)
# col=len(matrix[0])
# getmatrix()
# getboundary()
# diagonal=getdiagonal()
# if diagonal==getdiagonal(num):
#         print(matrix[i][j],end=" ")
# else:
#         print(" ",end=" ")
