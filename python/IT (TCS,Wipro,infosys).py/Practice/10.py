# LOW -> MAX -> LOW

list=[1,9,8,3,4,5]
# list.sort()
# print(list)

mp={}
max=0
for i in range(len(list)):
    mp[list[i]]=mp.get(list[i],0)+1
    if(list[i]>max):
        max=list[i]
print(mp)
print(max)
for key in mp.keys():
        if((key==max and mp[key]>1) or mp[key] > 2):
            print("False")
            exit(0)
print("True")