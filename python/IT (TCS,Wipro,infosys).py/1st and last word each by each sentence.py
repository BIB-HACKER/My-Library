#find word in sentence

# def word(latters):
#     a=[]
#     for i in latters:
        
#         a.append(i)
#         a.sort()
#     return' '.join(a)

# latters = "solve koro"
# print(word(latters))
 

def word(latters):
    
    for i in range(len(latters)):
        if i == 0:
           print(latters[i], end="")
        if i==len(latters) -1:
            print(latters[i], end="")
        if latters[i]==" ":
            print(latters[i-1],latters[i+1],end="") 

latters = input("enter a sentence-->")
word(latters)