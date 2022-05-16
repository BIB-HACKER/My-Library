def getsumanddifference(num1,num2=4):
    sum=num1+num2
    diff=num1-num2
    return sum,diff

#main

n1=int(input("enter first numer"))
n2=int(input("enter second numer"))
#function all with keyword arguments and parameter names must be same
sum,diff=getsumanddifference(n1)
print("sum ",sum)
print("difference ",diff)

#function call with keyword arguments order of passing does not matters
sum,diff=getsumanddifference(n1,n2)
print("sum ",sum)
print("difference ",diff)
