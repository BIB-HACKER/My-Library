s='aabccba'
ans=[]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        if s[i] not in ans:
           ans.append(s[i])
    if s[i-1]!=s[i]:
        ans.append(s[i])
  
print("".join(ans))

# for i in range(0,n):
#     temp=s[i]
#     while(temp==s[i]):
#         i+=1
#     ans+=temp
# print(ans)

# for i in range(0,len(s)):
#     for j in range(1,len(s)):
#         if s[i]==s[j]:
#             ans.append(s[i])
#             break

