# # INPUT A NUMEBR AND CHECK WEATHER THE NUMBER IS AVAILABLE IN THE LIST OR NOT USING LINER SEARCH
# num1 = eval(input("enter a list of 5 number"))
# num = int(input("enter a number in the list"))
# if num in num1:
#     print(num, "is available in the list")
# else:
#     print(num,"is not available in the list")

# #-----------------------------------------

# numlist =  eval(input("enter a list of 10 numers"))
# num = int(input("enter a number to search in the list"))
# for val in numlist:
#     if val==num:
#         print(num,"is available in the list")
#         break
# else:
#         print(num,"is not available in the list")

#---------------------------------------

list1 = eval(input("enter a 5 digit number list"))
num = int(input("enter a number search in the list"))
for i in range(0,len(list1)):
    if num==list1[i]:
        if num==list1[i]:
          print(num,"is available in the list and",i,"number index position")
else:
    # i =list1.count(num)
    # print(i,'time available in the list')
    print(num,"is found",list1.count(num), "time")
 
