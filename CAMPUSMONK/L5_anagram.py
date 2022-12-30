# Anagram means. input=> (str1-->(aabc)) and (str2-->(baac))
               # output=> (aabc)==(aabc)
str1=input("enter str1 words->")
str2=input("enter str2 words->")
a=[]
b=[]
for i in str1:
    a.append(i)
for i in str2:
    b.append(i)
a.sort()
b.sort()
if ' '.join(a)==' '.join(b):
    print("this is anagram string")
else:
    print("this is not anagram string")



  