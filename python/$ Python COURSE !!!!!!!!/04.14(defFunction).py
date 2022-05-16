def change():
    val=22
    print(val)
    # return val

#main
val=30
print(val)
change()
print(change())
print(val)

#/\/\/\/\/\/\/\/\/\/\/

num=1
def change():
    num=10
    # print(num)
    return num

#main
print(num)
print(change())
print(num)

# /\/\/\/\/\/\/\/\/\/\/\/\/

num=30
def display():
    print(num)
    print(num*2)
print(num)
display()

# /\/\/\/\/\/\/\/\/\/\

def test(n1,n2,n3=30):
# def test(n1=5,n2=5,n3=30):
    print(n1+n2+n3)
test(1,2,3)
test(1,2)
test(1)
test()

# /\/\/\/\/\/\/\/\/\/\/\/\

def display(l):
    l.reverse()
    print(l)
list=[1,2,3,4]
display(list)
print(list)

#/\/\/\/\/\/\/\/\/\/\

# from cgi import print_arguments


def display(num):
    num+=100
    print(num)
    return num
num=100
print(num)
display(num)
# print(display(num))
print(num) 




