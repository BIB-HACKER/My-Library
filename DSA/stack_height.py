# print x^n (stack height=n)

def calpower(x,n):
    if n==0:
        return 1
    if x==0:
        return 0
    return x * calpower(x,n-1)

x=2
n=5
ans=calpower(x,n)
print(ans)