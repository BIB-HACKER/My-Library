# list = eval(input("create a made list :"))
# unic = []
# dupli=[]
# for i in range(len(list)):
#     k = i+1
#     if list[i] not in list[k:]:
#         unic.append(list[i])
#     # else:
#     #     dupli.append(i)
# print("UNIC list is a :",unic)
# # print("DUPLICATE list is a ",dupli)

# list = [1,2,2,3,3,33,33,4,44,44,5,55,6,66,6]
# for i in range(len(list)-1):
# # print(list[2+1:])
#    if list[i] not in list[i+1:]:
#        print(list[i],end=" ")
# [1,2,2,3,4,4]
list = eval(input("create a made list :"))
N = len(list)
unic = []
dupli=[]
for i in range(N):
    k =  i+1
    for j in range(k,N):
        if list[i] == list[j] and list[i]:
            dupli.append(list[i])
        # else:
        #     unic.append(list[i])
# print(unic)
print(dupli)

######################

# list = eval(input("create a made list :"))
# unic = []
# dupli=[]
# for i in list:
#     if i not in unic:
#         unic.append(i)
# print(unic)