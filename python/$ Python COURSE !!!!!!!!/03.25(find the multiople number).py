#find multiple number to your chose number

# list1 = eval(input("enter few number in a list"))
# num= int(input("eneter a number"))
# match = 0
# for i in list1:
#     if i%num==0:
#         match+=1
#         print(i,"is a multiple number")

# if match==0:
#     print(num,"is not found in the list") 
# else:
#     print(num,"has found in the list")

    #--------------------------------------------------

list = eval(input("enter few number in a list"))
match = []
for i in range(1,len(list)):
    if list[i]%list[i-1]==0:
        match.append(list[i])
print("list of multliple is -",match)