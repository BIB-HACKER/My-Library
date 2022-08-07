x=int(input("value:"))
y=0
z=1
while z<=x:

   y+=z
   if z%2==0:
       print(z*3)
   else:
       print(z*2)
   z=z+1