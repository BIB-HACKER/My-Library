import math
v=6,3,6,20,3,6,-15,3,3
instr=v.split(",")
m=2
result={}
k=int(math.sqrt(len(instr)))
s1=0
s1_a=[]
l=[]
while(m<=k):
    j=()
    while(j<=len(instr)-(m*m)):
        matrix=[]
        i=j
        new_sum=()
        while(i!=(m*m)+j):
            matrix.append(instr[i:i+m])
            new_sum+=sum(instr[i:i+m])
            i+=m
            #print(matrix)

