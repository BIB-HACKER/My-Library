s="abcabe"
save=""
for i in range (0,len(s)):
    rept=0
    for j in range(0,len(s)):
        if i!=j:
            if s[i]==s[j]:
                rept=1
                break
    if rept==0:
       save+=s[i]+" "
       
if save!="":
    print("not repeating value is =",save)
else:
    print("not found")
    