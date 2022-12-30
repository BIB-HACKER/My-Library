def count_words(s):
    cnt=0
    for i in range(0,len(s)):
        if s[i]==" ":
            cnt+=1
    return (cnt+1)

s=input("enter your line->")
print(count_words(s))