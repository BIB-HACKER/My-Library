# num=int(input("enter number-->"))
# fact=1
# if num<1:
#     print("invalid number")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
# print(fact)

##################################

#recursion factorial

def fact(num):
    if num==0:
        return 1
    else:
        return (num * fact(num-1))


num=int(input("enter number-->"))
print(fact(num))