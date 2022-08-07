stri="CampusMonk"
o=""
l=len(stri)
for i in range(l):
    if i%2==0: #lowercase
        o+=stri[i].lower()
    else: #uppercse
        o+=chr(ord(stri[i])-32)

print(o)
    