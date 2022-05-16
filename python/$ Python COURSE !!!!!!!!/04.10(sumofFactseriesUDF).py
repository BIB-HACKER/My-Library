#find the sum fo the series s=1/1!+1/3!+1/5!+1/7!+.....10 times

def getfact(n): #return the factoral of n si knon as parametr/argumet
    fact=1
    for i in range(1,n+1):
        fact=fact+i
    return fact

def sum():
    sum=0
    deno=1
    for i in range(1,11):
        sum=sum+1/getfact(deno) #function
        deno+=2
    print("sum of the series :",sum)

#main block
sum() #method call