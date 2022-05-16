def getdiference(f1,f2):
               #formal parameter
    num=f1-f2
    print("difference ",num)

#main
f1=int(input("enter first number"))
f2=int(input("enter second number"))
getdiference(f1,f2)
getdiference(f2,f1)
            #actual parameter

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def getdiference(f1,f2):
                #formal parameter
    num=f1-f2
    return num

#main
f1=int(input("enter first number"))
f2=int(input("enter second number"))
print(getdiference(f1,f2))
print(getdiference(f2,f1))
                 #actual parameter

#/\/\/\/\/\/\/\/\/\/\/\
def adden(x,y,z):
    return x+y+z
    print(x+y+z)
print(adden(1,3,3))
