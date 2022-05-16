#sample output: Alphabets
#sample output:
#= = = = = = = = = = = = = = = = 
#Vowel frequency
#= = = = = = = = = = = = = = = = 
#a 2
#e 1

word=input("enter a word ->")
#convert to lower case
word=word.lower()
counta,counte,counti,counto,countu=0,0,0,0,0
print("-"*50)
print("-"*50)
print("Vowel Fequency")
print("-"*50)
print("-"*50)
#count the frequency in aloop
for ch in word:
    if ch=='a':
        counta+=1
    elif ch=='e':
        counte+=1
    elif ch=='i':
        counti+=1
    elif ch=='o':
        counto+=1
    elif ch=='u':
        countu+=1

# counta=word.count("a")
# counte=word.count("e")
# counti=word.count("i")
# counto=word.count("o")
# countu=word.count("u")

if counta>0:
    print('a->',counta)
if counte>0:
    print('e->',counte)
if counti>0:
    print('i->',counti)
if counto>0:
    print('o->',counto)
if countu>0:
    print('u->',countu)
