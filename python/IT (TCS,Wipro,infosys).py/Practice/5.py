L=[2,5,3,7,4,8,9,6]
l=len(L)-1
j=1
while j<=l:
    i=0
    while i<=l-j:
        if L[i]<L[i+1]:
            L[i],L[i+1]=L[i+1],L[i]
        i+=1
    j+=1

print(L)


