num=int(input("array size->"))
#--------
def min(a,b):
    if a>b:
        return a
    else:
        return b
#-------------
arr=[]
for i in range(0,num):
    arr.append(int(input("enter number =")))
#-----
mx=arr[0]
#-----
# for i in range(0,num):
#     if arr[i]>mx:
#         mx=arr[i]
# print("maximum number is ==>",mx)
#---------------------------------------
# print("maximum number is ==>",max(arr))    
#-------------------------------
#chreat minimum function
for i in range(0,num):
    mn=min(mx,arr[i])
print(mn) 
