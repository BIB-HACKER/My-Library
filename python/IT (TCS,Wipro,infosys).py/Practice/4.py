t="Mind@work!"
r=""
l=len(t)
print("original :",t)
for i in range(l):
    if t[i].isalpha()==False:
        r+="*"
    elif t[i].isupper()==True:
        r+=chr(ord(t[i])+1)
    else:
        r+=t[i+1]
    print("final :",r)