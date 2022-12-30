s="Bibhakar Paul"
o=""
for i in s:
    if i>='a' and i<='z':
        o+=chr(ord(i)-32)
    elif i==' ':
        o+=chr(32) 
    else:
        o+=chr(ord(i)+32)
print(o)