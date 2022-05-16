#Display all the person number in a range
#A numer which is equal to the sum of the factoral of each digit,is known as person/krishnamurty number

def displayallpetrsonos(low,high):#display all peterson number in a range
    print("peterson number between ", low, "to ", high, "are =")
    for num in range(low,high):
        if ispeterson(num)==True:
            print(num,end=" ")

def getfactoral(digit):
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    return fact

def ispeterson(num): #return true if num is a petrson number otherwise return false
    copy=num
    sum=0
    while copy>0:
        digit=copy%10 #extract a digit
        sum=sum+getfactoral(digit)#method call
        copy//=10
    if sum==num:
        return True
    else:
        return False

low=int(input("enter the lower range"))
high=int(input("enter the higher range"))
if low>high:
    print("invalid number")
else:
    displayallpetrsonos(low,high)#method call




# fact=1
# for i in range(1,0+1):
#     fact=fact*i
# print(fact)