# display the longest words in a list
words=eval(input("enter few words in a list"))
max=0
# find the length of longest word
for word in words:
    if len(word)>max:
        max=len(word)
# find the longest words
print("longest words are =",end=" ")
for word in words:
    if len(word)==max:
        print(word)