#(i) Display addition of tow dictionaries
#(ii) display subtraction of two dictionaaries
# EXAMPLE
# Enter first dictionary: dict1 = {'a': 10, 'b': 5, 'f': 33}
# Enter second dictionary: dict1 = {'d': 40, 'a': 15, 'f': 23}

import math
add={}
sub={}
dict1=eval(input("Enter the first dictionary"))
dict2=eval(input("Enter the second dictionary"))
#For addition
for key1 in dict1:
    if key1 in dict2:
        add[key1]=dict1[key1]+dict2[key1]
    else:
        add[key1]=dict1[key1]
for key2 in dict2:
    if key2 not in dict1:
        add[key2]=dict2[key2]

#For subtraction
for key1 in dict1:
    if key1 in dict2:
        sub[key1]=(int)(math.fabs(dict1[key1]-dict2[key1]))
    else:
        sub[key1]=dict1[key1]
for key2 in dict2:
    if key2 not in dict1:
        sub[key2]=dict2[key2]

print("Addition:",add)
print("Subtraction:",sub)