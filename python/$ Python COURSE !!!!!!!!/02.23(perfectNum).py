# num = int(input("enter positive numbr"))
# sum =0
# for i in range(1, num):
#     if num%i==0:
#         sum = sum+i
# if sum==num:
#     print(num,"this is perfect number")
# else:
#     print(num,"this is not perfect number")


# print("*********************************")

                                                       #
for count in range (1,101):                            # 
    num = count                                        #
    sum =0
    for i in range(1, num):
        if num%i==0:
            sum = sum+i
    if sum==num:
        print(num,"this is perfect number")
    else:
        print(num,"this is not perfect number")

##########################################

# count = int(input("choose numer"))
# for num in range(1,count+1):
#     sum = 0
#     for i in range(1,num):
#         if num%i==0:
#             sum = sum+i
#     if num==sum:
#         print(num,"is a perfect number")
#     else:
#         print(num,"is not a perfect numeer")
