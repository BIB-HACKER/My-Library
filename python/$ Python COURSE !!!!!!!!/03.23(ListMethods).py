l1 = [1,2,3,4]
print("the listis =", l1)
print("numaber fo elements in the list",len(l1))

l1.append(5)
print("after adding one element at the end of the list",l1)

l1.insert(0,"papon")
print("after adding one element at 0 index",l1)

l1.insert(9,6)
print("after adding one elements at the end of the list",l1)

l1.extend(["hacker",440])
print("after adding multiple elements at the end of the list",l1)

#list.pop(index) -delets the value at index position. it also return the value after deleting
val = l1.pop(7)
print("after deleting element at 7 index",val)
print("after deleting elements at 7 index",l1)

val= l1.pop()#autometicaly last element delet
print("autometicaly deleting at the last elements",l1)

l1.insert(0,4)
print(l1)

#l1.remove(value) 
#delets teh first occurrence of the value from the list , does not return anything
#produces error if not found
l1.remove(4)
print("after removing first occurrence",l1)

l1.remove("papon")
print("after removing first occurrence",l1) 

#list.clear() 
#to delete all elements of the list and the list becomes empty then
l1.clear()
print(l1) #empty list create

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

f1 = [5,1,5,3,8,0,6,7,3,2,5,3,4,5,6]
print("the list is",f1)

#count the occurrence if an element in the list-- list.count(value)
cnt = f1.count(3)
print("total count of 3",cnt)

f1.reverse()
print("after reversing the list",f1)

f1.sort()# arrange small elements to big elements. #arrange a list in asending order
print("after arrange the list",f1)

# f1.reverse()
# print(f1,"****************************")

f1.sort(reverse=True) # arrange a list descending order
print("after arrange the list in revrse order",f1)

print(sum(f1))
print(max(f1))
print(min(f1))