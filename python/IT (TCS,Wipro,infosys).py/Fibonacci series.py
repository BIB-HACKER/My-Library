fst=1
sed=2
print(fst,end=" ")
print(sed,end=" ")
while True:
    trd=fst+sed
    if trd>100:
        break
    print(trd,end=" ")
    fst,sed=sed,trd   # SWAP


