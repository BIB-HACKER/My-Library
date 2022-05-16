words=input("enter a sentnce->")
word=words.split()
maximum=0
for i in word:
    maximum=max(maximum,len(i))
    print(maximum)
print("word with maximum length are:-")
for i in word:
    if len(i)==maximum:
        print(i)