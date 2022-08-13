int1=3521
int2=2452
int3=1352

############## REVERSE STRING ##########################
# out=""
# for i in range(4):
#     if i%2==0:
#         out+=str(max({int1%10,int2%10,int3%10}))
#     else:
#         out+=str(min({int1%10,int2%10,int3%10}))
###############################################
############## REVERSE NUMBER ##########################
out=0
for i in range(4):
    if i%2==0:
        out+=pow(10,i)*(max({int1%10,int2%10,int3%10}))
    else:
        out+=pow(10,i)*(min({int1%10,int2%10,int3%10}))
    int1//=10
    int2//=10
    int3//=10

# print(out[::-1])
print(out)

