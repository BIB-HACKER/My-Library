def calculation(x,y=5):
    print(x)
    print(y)
    x=x*10
    y=x//y
    print(x,"*",y)
    return y
x=1000
y=22
x=calculation(x,y)
print(x,"$",y)
     