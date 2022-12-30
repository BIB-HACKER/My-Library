n=int(input("enter n value->"))
# 1st ferform the module operator to get the remainder 
# 2nd divided the number to ger the quotient
# 3rd store the remainder in an array
# so repeat the above steps till qotient becomes 0

# output the array elements in the reverse order
a=[]
count=0
for i in range(1,n+1):
    while i>0:
        rem=i%2
        a.append(rem)
        count+=1
        i//=2

for j in range(len(a)-1,0,-1):
    print(a[j],end="")