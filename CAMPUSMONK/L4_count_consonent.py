def count_words(s):
    cnt=0
    for i in range(0,len(s)):
        if s[i] not in "aeiouAEIOU":
            cnt+=1
    return (cnt)

s=input("enter your line->")
print(count_words(s))