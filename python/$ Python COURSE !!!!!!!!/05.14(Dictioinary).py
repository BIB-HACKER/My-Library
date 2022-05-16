from cv2 import DIST_C


dic={1:'ritam',2:'malay',3:'bibhakar'}
print(dic)
for key in dic:
    print(key,dic[key])
    print(key,dic.get(key))
#modify
dic[1]='golu'
#add
dic[5]='uuuu'
dic['x']='lplplp'
dic['v']=1
dic[6]=[1,2,3,4,5]
# dic[[1,2]]=234 #error
print(dic) 
print(len(dic))
print(dic.values())
print(dic.items()) #convert dictionary to 'list under Tuple'
Tuple=(dic.items()) 
for t in Tuple:
    print(t)  #DISPLAY THE TUPLE
print(1 in dic)
print('uuuu' in dic)
# Adding element in a dictionary
key=int(input('enter the rollno'))
value=input("enter a new name")
dic[key]=value
print('After a adding a new pair-->')
print(dic)
# delet element in a dictionary
key=(input('enter a key value'))
del dic[key]
print("after deleting key value-->")
print(dic)
#Updating element in a dictionary
key=(input("enter the key to search"))
value=input("eneter the new value")
dic[key]=value
print("after updating the dictionary is ")
print(dic)
copy=dic.copy()
print(copy)
print(len(copy))
