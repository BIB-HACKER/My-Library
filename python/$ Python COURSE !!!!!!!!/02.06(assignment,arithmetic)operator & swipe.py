# Arithmetic Operators : +,-,*,/(division),//(floor division),%(modulus),**(Exponentiation)
#FIRST RUN - **
#SECOND RUN - LEFT TO RIGHT(/,//,%,**)
#THERD RUN - +,-


       #use in arithmetic operator
       
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result=num1+num2
print("Addition=",result)
result=num1-num2
print("Subtraction=",result)
result=num1*num2
print("Product=",result)
result=num1/num2
print("Quotient=",result)
result=num1//num2
print("Quotient=",result)
result=num1%num2
print("Remainder=",result)
result=num1**num2
print("To the Power=",result)

####################################################################################

val = 10+4*3-4/2**2%5
# 10+4*3-4/4%5 = 10+12-4/4%5 = 10+12-1.0%5 = 10+12-1.0 = 22-1.0 = 21.0
print(val)

#####################################################################################

  #use in assignment operator

fst = 30
snd = 10
print("fisrt is =",fst)
print("second is =",snd)

snd+= fst #snd = snd+fst                          ADD->
print("snd is now snd+ = fst",snd)                 
snd-= (fst+5)  #snd = snd-fst                          SND VALUE ADD->
print("snd is now snd- = fst",snd)
snd*= 2  #snd = snd*2                          SND VALUE ADD->
print("snd is now snd* = fst",snd)
snd/= 2  #snd = snd/2                           SND VALUE ADD->
print("snd is now snd/ = fst",snd)
snd//= 2  #snd = snd//2                          SND VALUE ADD->
print("snd is now snd// = fst",snd) 
snd%= 2  #snd = snd%2                             SND VALUE ADD->
print("snd is now snd% = fst",snd)

###########################################################################

n1,n2,n3 = 23,34,564
print(n1+n2+n3)       # declearing many variable in same line

# ##############################################################################

   #4th genaretion swipe(INTERCHANGE) value logic

n1,n2 = 10,20
print("before swap= ")
print("n1=",n1,"and n2=",n2)

                  #3RD GENERATION INTERCHANGE LOGIC
# n1,n2=n2,n1      # doro = n1
n2,n1=n1,n2      # doro = n1
                 # n1 = n2
                 # n2 = doro

print("after swap= ")
print("n1=",n1,"and n2=",n2)

