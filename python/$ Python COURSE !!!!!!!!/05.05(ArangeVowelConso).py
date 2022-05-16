name=input("enter a word")
vowel=""
conso=""
for word in name: 
    if word in "AEIOUaeiou":
        vowel=vowel+word 
    else:
        conso=conso+word
newname=vowel+conso
print("new word is->",newname)
       