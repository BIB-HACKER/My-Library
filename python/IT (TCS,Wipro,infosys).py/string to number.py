words=input("enter a word->")
word=words.upper()
# WO=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z=1,2,3,4,5,6,7,8,9,(1+0),(1+1),(1+2),(1+3),(1+4),(1+5),(1+6),(1+7),(1+8),(1+9),(2+0),(2+1),(2+2),(2+3),(2+4),(2+5),(2+6)
# for i in word:
#     for j in WO:
# #     print(j)
#        if i==A:
#            print(A)
List=[]          
list=[]
for i in word:
    List.append(i)
    for j in range(65,99+1):
        if i==(chr(j)):
            list.append(str(j-64))
print(List)
print(list)
list1=[]
for i in list:
    if len(i)==1:
      list1.append(i)
    plus=0
    add=0 
    if len(i)==2:
        for j in range(len(i)):
            plus+=(int(i[j]))
        pol=str(plus)
        # print(pol)
        if len(pol)==1:
            list1.append(pol)
        else:
            if len(pol)==2:
                for p in range(len(pol)):
                    add+=(int(pol[p]))
                list1.append(str(add))

value=''
for i in list1:
    value+=i
print()
print(">->->->",value,"<-<-<-<")
print()
