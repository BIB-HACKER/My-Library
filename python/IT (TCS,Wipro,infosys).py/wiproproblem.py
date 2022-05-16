#4############################################
# Input :
# 8
# 10 98 3 33 12 22 21 11
# Output:
# 10 98 12 22 3 33 21 11
# All the even numbers are placed before all the odd numbers.

source = eval(input("create a list"))
# source = [10, 98, 3 ,33 ,12, 22 ,21, 11]
evennum =[]
oddnum=[]
#separate all the even and odd numbers
for val in source:
    if val%2==0:
        evennum.append(val)
    else:
        oddnum.append(val)

print(f"even and then odd numbers are :{evennum + oddnum}")
# print(f"odd numbers are :{oddnum}")

#28##########################################
# Input:
# 2514795
# Output:
# 162
# Odd digits in the given number 2514795 are 5, 1, 7, 9, 5. The sum of these odd digits is 27. Even digits in the given number 2514795 are 2, 4. The sum of these even digits is 6.
# So, the output is 162.

source = eval(input("create a list"))
odd=0
even=0
for i in source:
    if i%2==0:
        even+=i
    else:
        odd+=i

print(f"The output is { even*odd}")

###############################################################