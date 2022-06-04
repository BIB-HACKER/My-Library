dict={}
dict["Anisha"]=80
dict["Pradip"]=73
dict["purnendu"]=78
dict["kk"]=20
dict["cc"]=30
#traverse by loop
for key in dict:
    print(key,dict[key])
print(dict.keys()) #show keys
print(dict.values()) #show keys
print(type(dict.keys())) 
print(type(dict.values())) 
#Update
dict["Anisha"]=99
print(dict)
#deletion
del dict["kk"]
print(dict)
#del dict["kk"]
#search a key by membership operator
print("cc" in dict)
#deletion by pop()
print(dict.pop("cc"))
print(len(dict))
print(list(dict.items()))
print(dict)
newdict={"debayan":80,"Narottam":90}
dict.update(newdict) #concate 2 dictonary
print(dict)

##################################

d1={1:"integer",(1,2):"tuple","hi":"string"}
op=""
for key in d1:
    # print(key)
    op+=d1[key]+" "
print(op)
#####################################
d1={1:"integer",(1,2):"tuple","hi":"string"}
print(len(d1.values()),end=" ")
print(max(d1.values()))
######################################
d1={1:10,2:20,3:30,7:70}
n1=10
if n1 in d1.values():
    print("Found")
else:
    print("Not Found")