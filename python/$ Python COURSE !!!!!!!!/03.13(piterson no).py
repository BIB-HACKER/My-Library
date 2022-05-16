#Display all the 3 digit peterson number.
#A number is a petrson if sum of the factorial if digits is equal to the number.

import math
print("peterson number=")
num = 100
while num<=999:
    copy=num
    sum=0
    while copy>0:
        fact=1
        digit=copy%10
        fact=math.factorial(digit)
        sum+=fact
        copy=copy//10
    if num==sum:
        print(num)
    num+=1


# import math
# fact=1
# for i in range(1,5+1):
#     fact=fact*i
# # fact=math.factorial(5)
# print(fact)



