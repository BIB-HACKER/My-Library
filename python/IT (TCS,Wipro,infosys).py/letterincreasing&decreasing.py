# LETS CONDING!!!!!!!!!!!!!!!!!!!!!!!!!!

letter=input("type a word->")
rev=[]
even=(0,2,4,6,8,10,12,14,16,18,20)
odd=(1,3,5,7,9,11,13,15,17,19)
save=""
for i in range(0,len(letter)): 
    if i in even:
        if letter[i]=='z':
            rev.append(ord(letter[i])-25)
        elif letter[i]=='Z':
            rev.append(ord(letter[i])-25)
        else:
            rev.append((ord(letter[i])+1))
    elif i in odd:
        if letter[i]=='a':
            rev.append(ord(letter[i])+25)
        elif letter[i]=='A':
            rev.append(ord(letter[i])+25)
        else:
            rev.append((ord(letter[i])-1))
    
# print(rev)
add=[]
for i in rev:
    add.append(chr(i))
# print(add)

alt=""
for i in add:
    alt+=i
print()
print(f"So,{letter} will be coded as {alt}.")
# for i in save:
#     alt=""
#     for j in add:
#         alt+=i+'(+1)'+'->'+j+','
# print(alt)