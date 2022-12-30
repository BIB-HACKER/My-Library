s="1578"
sum=0
for i in range(0,len(s)):
    sum+=(int(s[i]))    # => 1+5+7+8  === 21
    # sum+=ord(s[i])-48  # => (49-48)=1+(53-48)=5+(55-48)=7+(56-48)=8 === 21

print(sum)