# BUILT -IN MATHEMATICLAL FUNCTION
print(len([1,2,3,4]))
print(pow(2,4))          #############      
print(pow(2.5,5))        #############
string=str(1234)
print(len(string))
# convert a float to an int
num=int(34.45)
print(num)
# convert a string having int to an int number
num=int("123")
print(type(num))
num=float("123.456")
print(num)
# return the type pf an object
print(type(12))
# return the absolute value of a float/int
print(abs(-34.4))        #############
# return 2 complex numbers as parameter and return of pair of numbers consisting of
#their quotient and remainder
print(divmod(45,5))       ################
print("sum of list elements and 10",sum([1,2,3,4,5],10))
print("maximum among list elements",max([1,2,3,4,5]))
print("maximum among tuple elements",max((1,2,3,4,15,0)))
print("maximum among list elements",min([1,2,3,4,5]))
print("maximum among list elements",min((1,2,3,4,5)))
num=32
# converts to octal
print(oct(num))
# convert to hexadecimal
print(hex(num))
print(round(12345,2))
print(round(12345.6789,2))
# built in string function
# syntax str join(string)- concatenates str after each character of string
print("??".join("python"))
print("python".join("??"))
# str.replace(string1,string2) peplace every occurce of string1 by string2 in str
# SEARCHING IS CASE SENSITIVE HERE
print("condig is my passion.coding is my passion".replace("ing","ping"))
print("condig is my passion.coding is my passion".replace("ING","PING"))
print("condig is my passion.coding#is#my#passion".split("#"))
