def sumsqrdigit(num):
    x=int(num)
    n=0
    while(x>0):
        rev=x%10
        rev*=rev
        n+=rev
        x=x//10
    print(n)
    return n

def rotateright(string):
    n=""
    x=""
    n+=string[:-1]
    x+=string[-1]
    x+=n
    return x

def rotateleft(string):
    n=""
    x=""
    n+=string[:2]
    x+=string[2:]
    x+=n
    return x

series=("ghftd:1246").split(':')

for i in series:
    if (i.isdigit()):
        n=i
    else:
        stg=i

if(sumsqrdigit(n)%2==0):
    print(rotateright(stg))
else:
    print(rotateleft(stg))

# o=""
# y=""
# x="ghftd"
# o=x[:2]
# y=x[2:]
# print(y+o)
