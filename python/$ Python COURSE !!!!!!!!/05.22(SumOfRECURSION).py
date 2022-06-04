#recursion
#find the sum of first n natural nos
def getsum(n):
    if n==0:  #base criteria
        return 0
    else:
        return n+getsum(n-1)  #recursive call # 2+1+getsum(0)

#INPUT->5 AND CALLED getsum(5)
#return 5+ getsum(4)
#return 5+ return 4+ getsum(3)
#return 5+ return 4+ return+3+ getsum(2)
#return 5+ return 4+ return 3+ return 2+ getsum(1)
#return 5+ return 4+ return 3+ return 2+ return 1 + getsum(0)
#return 5+ return 4+ return 3+ return 2+ return 1 + 0
#return 5+ return 4+ return 3+ return 2+ 1
#return 5+ return 4+ return 3+ 3
#return 5+ return 4+ 6
#return 5+ 10
#return 15


n=int(input("Input n->"))
sum=getsum(n)  #method call
print("sum of the",n,"natural nos is=",sum)
