# #input a number and check weather the number is a prime no.or not

import math
num = int(input("enter a positive number"))
if num<=0:
    print("invalid number")
else:
    count=2
    if num==1:
        print("it is neither prime nor a composite number")
    else:
        # while count< math.sqrt(num):#num: 
        while count< num:#num: 
            if num%count==0:
                print("not a prime number")
                break
            count+=1
        else:
            print("it is a prime number")




# count = 2
# while count<=10:
#     co = count
#     if co:
#        print(co)
       
#     count+=1

