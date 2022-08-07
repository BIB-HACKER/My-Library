B="CD#34"
# B="12ab"
sum=0
for i in B:
    if i.isdigit()==True:
        sum+=int(i)
    # elif i==
    else:
        p=str(ord(i))     # find the maximum digit and sum this digit
        o=[]
        for j in p:
            o.append(int(j))
        sum+=max(o)
        # print(o)
        o=[]
        ##########################################
        # p=ord(i)
        # print(p)
        # max=0
        # while p>0:
        #     max=p%10
        #     p//=10
        #     print("***",max)
        # sum+=max

print(sum)

# p="97"
# # print(p)
# o=[]
# sum=0
# for j in p:
#     o.append(int(j))
# sum+=max(o)
# print(sum)