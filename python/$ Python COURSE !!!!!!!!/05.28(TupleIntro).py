# create an empty tuple
from numpy import maximum


t1=tuple()
print(t1)
t1=()
print(t1)
# create a tuple which consist of only one integer
t2=(1,)
print(t2)
# create a tuple which consists of three integer
t2=(9,2,3)
print(t2)
t2=(1,2,3,"HI",5.0)
print(t2)
t2=("mam","me","other","we")
print(t2)
# creating tuple form a list
t2=tuple([1,2,3])
print(t2)
l1=[1,2,3,4,5]
t2=tuple(l1) # when Tuple declare output in tuple
print(t2)
t2=(l1) # when tuple not declare outpout in List
print(t2)
# careating tuple from a string
name='bibhakar'
t2=tuple(name)
print(t2)
# length tuple from a string
length=len(t2)
print(length)
# find sum value
t2=(1,10,3,300,-9,900,7,77,900)
s=sum(t2)
print("total of all tuple elements",s)
newtuple=sorted(t2) # create new sorted list,origianl one remains same
print("sorted tuple is=",newtuple)
print("Original tuple is=",t2)
# find maximum vlaue
maximum=max(t2)
print(maximum)
#find minimum vlaue
minimum=min(t2)
print(minimum)
# find index of a number
pos=t2.index(300)
print(pos)
# print(t2.index(300))
# find ferquency of a number in a tuple
cnt=t2.count(900)
print(cnt)
# print(t2.count(900))
