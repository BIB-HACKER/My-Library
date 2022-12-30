# print the fibonacci sequence till nth term*

def printfb(a,b,n):
    if n==0:
        return
    c=a+b
    print(c)
    printfb(b,c,n-1)

a=0
print(a)
b=1
print(b)
n=5
printfb(a,b,n)