#input a number and check weather the number is a disarium number or not . e.g: 135 is a disarium number

num = int(input("enter positive number"))
sum = 0
copy = num
count = 0
digit=0
#this loop counts total number of digits 
while copy>0:
    copy=copy//10
    count+=1   #count total number of digits
# print(copy)
# print(count)
copy=num
#this loop calculate the sum of the digits raised to the power of the position
while copy>0:
    digit=copy%10 #to get the digits of one's place
    sum+= digit**count 
    count-=1
    copy//=10
    
if num==sum:
    print("it is a Disarium number")
else:
    print("it is a not Disarium number")