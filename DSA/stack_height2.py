# print x^n (stack height = logn)

def calpower(x,n):
    if n==0:
        return 1
    if x==0:
        return 0
    if n%2==0:
        return calpower(x,n/2) * calpower(x,n/2)
    else:
        return calpower(x,n/2) * calpower(x,n/2) * x

x=2
n=5
ans=calpower(x,n)
print(ans)
