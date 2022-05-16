# fact = 2
# num = int(input('enter positive number'))

# if num<1:
#     print('invalid input')
# else:
#     for count in range(1,num+1):
#         print(fact)
#         fact = fact*count
#     print(f"factorial of num is {num} and fact is {fact}")

###############################################################################

fact = 2
num = int(input('enter positive number'))

if num<1:
    print('invalid input')
else:
    for count in range(1,num+1):
        fact = fact*count
        print(fact)
    print(f"factorial of num is {num} and fact is {fact}")
