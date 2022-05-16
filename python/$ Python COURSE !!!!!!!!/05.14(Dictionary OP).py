fruit={}
L1=["apple","banna","apple"]
for index in L1:
    if index in fruit:
        fruit[index]+=1
    else:
        fruit[index]=1
print(len(fruit))
print(fruit)
#######################
arr={}
arr[1]=6
arr['1']=2
arr[1]=23
print(arr)
sum=0
for i in arr:
    sum+=arr[i]
print("sum of values =",sum)
########################
a={(1,2):10,(3,2):100}
print(a[(3,2)])
####################
b={'a':1,'b':2,'c':3}
print(b['a'],b['c'])
print(1 in b.values()) #there 1 is a vlaue
print('a' in b) # there 'a' is a key