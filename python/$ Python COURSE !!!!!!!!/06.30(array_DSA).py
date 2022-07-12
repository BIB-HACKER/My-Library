import array as A

# obj=A.array('i',[45,-5,7,9])
# for val in obj:
#     print(val,end=" ")

# print()
# for index in range(0,obj.itemsize):
#     print(obj[index],end=" ") 

# print()
# obj.append(33)
# print(obj)
# print(obj.pop(4))
# obj.remove(7)
# print(obj)
# L=[3,7,46,-45,-7]
# obj.fromlist(L)
# print(obj) 
# # o=[3,7,46,'a',(3,4)]    #ERROR variable type vlaue
# # obj.fromlist(o)
# # print(obj)
# obj.reverse()
# print(obj.itemsize)

# ####################################

# List=[3,5,6,-2,-65,-8,-9]
# obj=A.array('i',List)
# # e=[]
# # o=[]
# e=0
# o=0
# for i in obj:
#     if i>0:
#         # e.append(i)
#         e+=1
#     else:
#         # o.append(i)
#         o+=1

# # print("positive is ",len(e))
# # print("Negetive is ",len(o))
# print("positive is ",e)
# print("Negetive is ",o)

########################################

obj=A.array('b',[0,-128,1,127]) #signed integer(- or +)[1byte half value()]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('B',[0,255]) #usigned integer(+)[1byte full value()]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('u',['a','e','1','0','2','9','z','Q','/','!','$','&']) #unicode character[2 byte]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('Q',[10000000000000000000,9999999999999999999]) #usigned integer(+)[8byte full value()]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('q',[-1000000000000000000,999999999999999999]) #signed integer(- or +)[8byte half value()]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('I',[0,1000000000,999999999,1111111111]) #usigned integer(+)[2byte full value()]
for val in obj:
    print(val,end=" ")
print()
obj=A.array('i',[0,-1000000000,-999999999,-1111111111]) #signed integer(+ or -)[2byte full value()]
for val in obj:
    print(val,end=" ")
print()