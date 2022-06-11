# Each letter of an input string using dictionary.
# Also display the numeber of vowels and consonants string.
# in the given string.
# orignal string: Alligator output: A A G I L L O R T
# A - 2
# G - 1
# I - 1
# L - 2
# O - 1 
# R - 1
# T - 1

word=input("Original String->")
# length=len(word)
# string to list conversion
list=list(word.upper())
list.sort()
print(list)
#create empty dictionary
dict={}
# count the frequency and add to the dictonary
for char in list:
    dict[char]=list.count(char)
# print(dict)
# Display
print("Output")
for key in dict:
    print(key,"-",dict[key])

# A STIRNG CONTAINING ALL THE VOWELS
vest="AEIOU"
vcount=0 #it is used to count vowels
ccount=0
word=word.upper()
# Count total number of vowels 
for ch in word:
    if ch.isalpha():
        if ch in vest:
            vcount+=1
        else:
            ccount+=1

print("total number of VOWELS=", vcount)
print("total number of CONSONANTS=", ccount)