def union(a,b):
    # o=[ ]
    # for i in a:
    #     o.append(i)
    # for j in b:
    #     if j not in o:
    #        o.append(j)
    # return o
    o=""
    for i in range(0,len(a)):
        o+=str(a[i])+" "
    for i in range(0,len(b)):
        present=False
        for j in range(0,len(a)):
            if b[i]==a[j]:
                present=True
        if present==False:
            o+=str(b[i])+" "
    return o
def intersection(a,b):
    p=[]
    for i in a:
        for j in b:
            if i==j:
                p.append(j)
    return p

arr1=[2,3,9,18,5]
arr2=[5,9,60,4]
print(union(arr1,arr2))
print(intersection(arr1,arr2))