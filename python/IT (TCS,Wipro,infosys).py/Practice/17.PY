# Armstring sumber

num='153'
copy=num
sum=0
for i in range(0,len(num)):
    sum+=pow(int(num[i]),len(num))
# print(sum)
ans=0
num=int(num)
if int(copy)==sum:
    print(f"{num} is a Armstring sumber")
    while num!=0:
        if((num%10)%2)==0:
           ans+=num%10
        num//=10
else:
    print(f"{num} is a not Armstring sumber")
    while num!=0:
        if((num%10)%2)!=0:
           ans+=num%10
        num//=10
    
print(ans)
