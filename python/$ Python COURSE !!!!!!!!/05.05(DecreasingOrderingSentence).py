#lingth wise sorting#################################

words=input("enter a sentnce->")
# words="my country is the best in the world"
word=words.split()

mini=[]
minimum=""
for i in word:
    mini.append(len(i))
    mini.sort()
list=[]
for x in mini:
    if x not in list:   
        list.append(x)   
print(list)       
for i in list:
    for j in word:
        if i==len(j):
            minimum=minimum+j+" "
print(minimum)

