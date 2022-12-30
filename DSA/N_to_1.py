def printab(n):
    if n==0:
        return 0
    print(n)
    printab(n-1)

n=7
printab(n)
