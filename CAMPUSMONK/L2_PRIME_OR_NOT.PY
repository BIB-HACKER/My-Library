def isprime(num):
    if num==0:
        # print("invlaid number")
        return False
        # return ("invlaid number")
    # if num==1:
        # print(f"{num} is neither prime nor a composite number")
    for i in range(2,num):
        if num%i==0:
            # print(f"{num} is not a prime number")
            return False
            # return (f"{num} is not a prime number")
            # break
    else:
        # print(f"{num} is a prime number")
        return True
        # return (f"{num} is a prime number")

# num=int(input("enter number->"))

# val=isprime(num)
# if val==False:
#     print(f"{num} is not a prime number")
# else:
#     print(f"{num} is a prime number")

# print(isprime(num))

a=2
b=15
for i in range(a,b+1):
    if isprime(i):
        print(i)