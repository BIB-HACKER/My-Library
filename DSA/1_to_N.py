# print 1 to n & back print n to 1

def printnum(n):
    if n==6:
        return 
    print(n)
    printnum(n+1)

n=1
printnum(n)
############################
# def printnum(n):
#     if n==6:
#         return 
#     printnum(n+1)
#     print(n)

# n=1
# printnum(n)