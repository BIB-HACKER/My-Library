def fun(a,b):
    if (b>7 & (1+a)>(a^b)):
        a=3+a+b
        b=(a+2)+b
        return b+fun(b,a)-a+2
    a=b+2
    return a

print(fun(9,9))