import random
low=25
point=5
p=""
for i in range (1,5):
    if i<4:
       number=(str(low+random.randrange(0,point))+":")
       p+=number[0:3]
    else:
       number=(str(low+random.randrange(0,point))+":")
       p+=number[0:2]

    point=1
print(p)