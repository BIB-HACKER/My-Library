# find the number of ways to reach the end(#)

def paths(i,j,n):
    if i<0 or j<0 or i>=n or j>=n:
        return 0
    if i==n-1 and j==n-1:                           # paths(0,0,2)      
        return 1                        #          _______/\________
    ways=0                             # paths(1,0)             paths(0,1)
    ways+=paths(i+1,j,n)               #      /\                      /\
    # print(ways,end="*")        #  paths(2,0)  paths(1,1)  paths(1,1)  paths(0,2)
    ways+=paths(i,j+1,n)         #      |          |           |            |
    # print("\n",ways,end="#")  #    return 0   return 1   return 1      return 0
                                        
    return ways                  # print(1+1)  

n=int(input("enter number-->"))
print(paths(0,0,n))