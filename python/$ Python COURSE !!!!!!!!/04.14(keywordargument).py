#usr-defined function and keyword/named argument
#position are same

def getsumanddifference(n1,n2):
    sum=n1+n2
    diff=n1-n2
    return sum,diff

#main


#function all with keyword arguments and parameter names must be same
sum,diff=getsumanddifference(n1=10,n2=20)
print("sum ",sum)
print("difference ",diff)

#function call with keyword arguments order of passing does not matters
sum,diff=getsumanddifference(n2=30,n1=50)
print("sum ",sum)
print("difference ",diff)
