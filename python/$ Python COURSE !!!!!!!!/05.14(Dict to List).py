dict={1:"hi", 2:"bye"}
copy={3:"bye"}
# copy=dict
# print(copy)
# copy.pop(2)
# print(copy)
dict=copy
print(dict)
dict[2]="come"
print(dict)
print(dict.pop(2))
print(dict)
l=list(dict.items())
print(l)
print(1 in dict)
print("bye" in dict) #value False
print("bye" in dict.values()) #value True