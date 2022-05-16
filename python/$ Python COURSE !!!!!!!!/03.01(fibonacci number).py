#display all the fibonacci numbers between 0 and 100
#fibonacii series---0,1,2,3,4,5,6,7,8..

# first = 0 
# second = 1
# print("all the fibonacci number between 0 and 100 are")
# print(first)
# print(second)
# while True:
#     third=first+second
#     if third>100:
#         break
#     print(third,end="")
#     first=second
#     second=third

#########################################
first = 0 
second = 1
print("all the fibonacci number between 0 and 100 are")
print(first)
print(second)
third = 0
N = int(input("ENTER YOUR NUMBERS"))
for i in range(0,N):
    third = first+second
    print(third,end=" ")
    first=second
    second=third
# res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))

#####################################

# import math
# N = int(input())
# def make_fibonacci(n):
#     a,b = 0,1
#     for i in range(N):
#         c = a+b
#         print(c)
#         a , b = b , a+b
#         return tuple(c)
        
