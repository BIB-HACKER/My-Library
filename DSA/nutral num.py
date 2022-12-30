# print sum of first n natural numbers

def printsum(i,n,sum):

    if i==n:
        sum+=i
        print(sum)
        return
    sum+=i
    printsum(i+1,n,sum)
    print(i)

printsum(1,5,0)