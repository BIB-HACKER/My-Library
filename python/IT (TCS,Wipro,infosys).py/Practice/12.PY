# SUM OF ARRAY/LIST USING RECURTION

def sum(index,list):
    if index>=len(list):
        return 0
    return list[index]+sum(index+1,list)

list=[3,2,1,8,10]
index=0
print(sum(index,list))