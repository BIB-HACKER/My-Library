#ENTER NAMES OF 5 STUDENT IN A TUPLE AND THEN SEARCH FOR A PRTICULAR NAME
# IF FOUND THEN DISPLAY "NAME FOUND" ELSE DISPLAY "NAME NOT FOUND" 

names=eval(input("enter names of 5 students->"))
search=input("enter a name to search->")
# for name in names:
#     if name.upper()==search.upper():
#         print("name found")
#         break
# else:
#     print("name not found")

###########################
new=sorted(names)
print(new)
if search in new:
    print("name found")
else:
    print("not found")