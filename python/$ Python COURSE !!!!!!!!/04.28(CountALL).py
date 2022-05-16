# input a sentence and count total number of vowel,consonant,digit
#and special characters present in each word.

line=input("enter a line ->")
words=line.split() #haere words is a list of string
print('-'*60)
print("word   \tvowel\t consonant\tdigit\t  specialcharacter")
print('-'*60)
for word in words:
    vowel,conso,digit,special=0,0,0,0
    for ch in word:
        if ch.isdigit():
            digit+=1
        elif ch.isalpha():
            if "AEIOU".find(ch.upper())!=-1:
                vowel+=1
            else:
                conso+=1
        else:
            special+=1      
    print(word,"\t",vowel,'\t   ',conso,'\t\t',digit,' \t      ',special)    