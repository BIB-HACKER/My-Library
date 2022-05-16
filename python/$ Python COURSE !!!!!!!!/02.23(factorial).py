num = int(input("enter number"))
if num<1:
    print("Envalid number")
else:
    # i = 1
    fact =1
    # while i<num:
    #     fact = fact*i
    #     i = i+1
    #     print(fact)

#     # print(f"factorial count of {num} and totla fact is {fact}")

# num = int(input)
# for i in range(1,num):
#     fact = fact*i
#     print(fact)

################################################

#Return the factorial of the number N=10

def factorial(N):
     if (N <= 1):
         return 1;
     else:
         return (N * factorial(N - 1));