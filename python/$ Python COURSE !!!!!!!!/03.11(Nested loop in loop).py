#nested loop

# 1 1
# 1 2
# 1 3
# 4 1
# 2 1
# 2 2
# 2 3
# 4 2
# 3 1
# 3 2
# 3 3
# 4 3
# 4 1
# 4 2
# 4 3
# 4 4
# 5 1
# 5 2
# 5 3
# 4 5

# i = 1
# while i<=5:
#     j = 1
#     while j<=3:
#         print(i,j)
#         j+=1
#     print(j,i)
#     i+=1

# #######################

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 4 1
# 4 2
# 4 3
# 5 1
# 5 2
# 5 3

# for i in range (1,6):
#     for j in range(1,4):
#         print(i,j)

#############################

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for row in range(1,10):
#     for i in range(1,row+1):
#         print(row,end="")

#     print() 

# ###################################

# 12345
# 1234
# 123
# 12
# 1

#outer loop
# for b in range(5,0,-1):
# for b in reversed(range(1,6)):
#     #inner loop
#     for p in range(1,b+1):
#         print(p,end="")

#     print()
#    #********
# for j in range(5,0,-1):
#    for i in range(1,j+1):
#         print(i,end="")

#    print() 
      #************
# for j in range(1,6):
#    for i in range(1,7-j):
#         print(i,end="")

#    print() 

# for i in range(1,6-1):
#         print(i,end="")


######################

# A
# AB
# ABC
# ABCD
# ABCDE

#outer loop
# for i in range (65,70):
#     #inner loop
#     for j in range (65,i+1):
#         print(chr(j),end="")

#     print()

# #############################

# B
# BI
# BIB
# BIBH
# BIBHA
# BIBHAK
# BIBHAKA
# BIBHAKAR

# olo = "BIBHAKAR"
# for i in range (0,8):
#     for j in range (0,i+1):
#         print(olo[j],end="")

#     print()

#################################

# 55555
# 4444
# 333
# 22
# 1

# for row in range(5,0,-1):
#     for i in range(1,row+1):
#         print(row,end="")

#     print() 
     #***********
# for j in range(5,0,-1):
#    for i in range(1,j+1):
#         print(j,end="")

#    print() 

#####################################

# 54321
# 5432
# 543
# 54
# 5

# for j in range(1,6):
# #    for i in reversed(range(j,6)):
#    for i in range(5,j-1,-1):
#         print(i,end="")

#    print() 

# for i in range(1,6):
#         print(i,end="")

#####################################

# 13579
# 1357
# 135
# 13
# 1

# for i in range(10,0,-2):
#    for j in range(1,i,+2):
#         print(j,end="")
#    print()
#        #*******
# for i in range(9,0,-2):
#    for j in range(1,i+1,+2):
#         print(j,end="")
#    print()


# for i in range(10,-1,-2):
#     print(i)
# for count in range(9,0,-2):
#     print(count)  

################################

# 45678
# 4567
# 456
# 45
# 4

# for b in range(1,6,+1):
# # for b in reversed(range(1,6)):
#     #inner loop
#     for p in range(4,10-b):
#         print(p,end="")
#     print()

############################################

# @ @ @ @
# @ ? ? @
# @ ? ? @
# @ @ @ @

# for row in range (1,5):
#       for col in range(1,5):
#             if row==1 or row==4 or col==1 or col==4:
#                   print('@',end=" ")
#             else:
#                   print('?',end=" ")
#       print()

############################################

# @ @ @ @ @ @ @
# @ ? ? @ ? ? @
# @ ? ? @ ? ? @
# @ @ @ @ @ @ @
# @ ? ? @ ? ? @
# @ ? ? @ ? ? @
# @ @ @ @ @ @ @

# for row in range (1,8):
#       for col in range(1,8):
#             if row==1 or row==4 or row==7 or col==1 or col==4 or col==7:
#                   print('@',end=" ")
#             else:
#                   print('?',end=" ")
#       print()

##############################################

# 2
# 4 4
# 6 6 6
# 8 8 8 8 

# for row in range(1,5):
#       for col in range(1,row+1):
#             print(row*2,end=" ")
#       print()

################################################

# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?
# @ ? @ ? @ ? @ ? @ ? @ ?

# lines = int(input("how many lines to print"))
# for row in range(1,lines+1):
#       for col in range(1,lines+1):
#             if col%2==1:
#                   print('@',end=" ")
#             else:
#                   print('?',end=" ")
#       print()