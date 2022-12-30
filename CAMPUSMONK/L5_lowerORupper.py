a = "Bibhakar"

# p=""     #lower to upper
# for i in range(0,len(a)):
#     if ord(a[i])>=ord('a') and ord(a[i])<=ord('z'):
#           p+=chr(ord(a[i])-32)
#     else:
#         p+=a[i]        
# print(p)
    #-----------------------
# o=[]   #lower to upper
# for i in a:
#     if i>='a' and i<='z':
#         o.append(chr(ord(i)-32))
#     else:
#         o.append(i)
# print(''.join(o))
    #---------------------------
o=[]   # upper TO LOWR
for i in a:
    if i>='A' and i<='Z':
        o.append(chr(ord(i)+32))
    else:
        o.append(i)
print(''.join(o))
#----------------------------
print()
print(a.upper())
print(a.lower())



