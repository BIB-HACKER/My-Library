# Write a python progaram to remove duplicate words from a given string and display the resultant string 
# In ascending order

# def remove(string):
#     l =string.split(" ")
#     list=[]
#     for x in range(0,len(l)):
#         # for j in range(0,len(l)):
#             if l[x] not in l[x+1:]:   
#                list.append(l[x])
#                list.sort()
#     return ' '.join(list)

# string="Next Time There Won't Be A Next Time"
# print(remove(string))


def remove(string):
    l =string.split(" ")
    list=[]
    for x in range(0,len(l)):
        if l.count(l[x])==1:   
            list.append(l[x])
            list.sort()
            print(list)
    return ' '.join(list)

string="Next Time There Won't Be A Next Time"
# string=str(input("enter duplicate valuae =>"))
print(remove(string))

