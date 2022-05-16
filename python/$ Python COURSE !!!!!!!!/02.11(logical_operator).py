#LOGICLA OPERATORS- and, or, not
     
"""
      1> "and" output 'TRUE' -> when both side is TRUE & output 'FALSE' -> when one side TRUE and other side is FALSE
      2> "or" output TRUE -> when both side is TRUE & both side is FALSE/TRUE
      3> "not" when input TRUE/FALSE -> output FALSE/TRUE
"""

age = 25
result=age>13 and age<20
print("age =",age,"years")
print("age>13 and age<20 =",age>13 and age<20)

c1=22
print("class=",c1)

result= c1==10 or c1==22
print("c1==10 or c1==22 =",result)

result= not(c1==22)
print("not(c1==22) =",result)

result= not 22>44 or 3==4 and 9!=8
print("not 22>44 or 3==4 and 9!=8 =", result)

result= not ((22>44 or 3==4) and 9!=8)
print("not ((22>44 or 3==4) and 9!=8) =",result)

re= not not 20>10
print(re)

re= not not 20<10
print(re)

re= not not not True
print(re)

print(3!=9 and "hello planet")
print(3==9 and "hello planet")
print(3!=9 or "hello planet")
print(3==9 or "hello planet")