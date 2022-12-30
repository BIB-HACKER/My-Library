#print Factorial of a number n

def calcfactorial(n):
    if n==1 or n==0:
        return 1
    return n* calcfactorial(n-1)

n=5
ans=calcfactorial(n)
print(ans)