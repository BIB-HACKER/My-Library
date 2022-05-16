texts=input("enter a text-->")
text=texts.upper()

list=[]
list1=[]
for i in text:
       if i=='Z':
            list.append(ord(i)-25)
       elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXY':
                list.append((ord(i))+1)
for j in list:
    list1.append(chr(j))
print(list1) 
out=""
for i in list1:
    out+=i

print(">->",out,"<-<")
