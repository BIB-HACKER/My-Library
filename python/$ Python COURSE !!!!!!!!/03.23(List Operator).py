from multiprocessing import Condition


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [9,8,7,6,5,4,3,2,1]

#concatenation of two list
#Condition(concatenation operator only work [2 list], when [list+list+3] show error)
l3 = l1+l2
print(l3)

# replication of a list
#Condition(replication order only successfuly show when [list*number],(when [list*list] error show))
l4 = l2*3 # (*)ASTERIC Operator
print(l4)

#SLICING
#list[start indedx:end index:step index]
print(l1[1:8])# GET ALL THE ELEMENTS FROM INDEX 1 TO 8
print(l1[:8])# GET ALL THE ELEMENTS FROM INDEX 0 TO 8
print(l1[1:])# GET ALL THE ELEMENTS FROM INDEX 1 TO LAST ELEMENTS
print(l1[1:8:2])
print(l1[-1:-10:-1])# traversing by negative index
print(l1[::2])
print(l1[2::2])
