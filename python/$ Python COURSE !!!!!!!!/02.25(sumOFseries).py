# #find sum of the serice sum 1/2 + 2/3 + 3/4......10 times

sum = 0
numerator = 1

while numerator<=10:
    sum = sum+ numerator/(numerator+1)
    numerator+=1
    # numerator = numerator+1

    print(sum)

# print()
# print("****************************")
# print()

sum = 0
numerator = 1

for i in range(numerator,11):
    sum = sum+ numerator/(numerator+1)
    # numerator+=1
    numerator = numerator+1

print(sum)

# print()
# print("********************************")
# print()

# #find the sum of the following serice-
# #sum-(a+1)^2/5 + (a+3)^4/10 +(a+5)^6/15 + (a+7)^8/20 .......n terms
 
a = int(input("enter the valur if a"))
n = int(input("enter the number of terms"))
sum= 0
for i in range (1,n+1):
    sum = sum+(a+i*2-1)**(i*2)/(i*5)
    print(f"sum series is {sum}")

# print()
# print('''**********************************''')
# print()

a = int(input("enter the valur if a"))
n = int(input("enter the number of terms"))
sum = 0
i = 1
# for i in range (1,n+1):
while i<=n:
    sum+=(a+i*2-1)**(i*2)/(i*5)
    i+=1
print(f"sum series is {sum}")

# print()
# print("***************************")
# print()

sum = 0
for i in range (1,11):
    sum+= i/(i*5)
    print(f"total sum is {sum}")

# print("###############################")

sum = 0
i = 1
while i<=10:
    sum+= i/(i*5)
    i+=1
    # print(f"total sum is {sum}")
    print("sum of series is",sum)
print(f"total sum is {sum}")

#########################################################

sum = 0
n = int(input("enter the terms number"))

for i in range(1,n+1):
    sum = (i*i)+1
    print(sum)

# #########################################################


sum = 0
n = int(input("enter the terms number"))

for i in range(1,n+1):
    sum = i*(i+1)
    print(sum)

# #########################################################

sum = 3
n = int(input("enter the terms number"))

for i in range(1,n+1):
    print(sum)
    sum = sum*2

# ####################################################

x = int(input("enter the value of X "))
sum = 0
for i in range(1,11):
    sum+= x/((i*2)-1)
print("the series of sum is", sum)

print()

# x = int(input("enter the value of X "))
sum = 0
for i in range(1,11):
    sum = (i*2)-1
    print(f"{x}/{sum}")

# ######################################################

sum = 0

for i in range(1,20):
    sum+= i/(i+1)
print(sum)
print((f"{i}/{sum}"))

sum = 0

for i in range(1,20):
    sum = (i+1)
    print((f"{i}/{sum}"))

# ####################################################

sum = 1
n = int(input("enter the terms number"))

for i in range(1,n+1):
    print(sum)
    sum+= sum
print(sum,end="")
