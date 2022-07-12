# letter = '''dear <|name|>,
# you are selected!
# world most top franchis hacking leag.
# now you are the most excepencip man in the world.
# indin most loved man!!!!!!!!!!!!!!!!!!
# date: <|date|>
# '''



# name = input("enter your name\n: ")
# date = float(input("enter date\n: "))

# letter = letter.replace("<|name|>",name)
# letter = letter.replace("<|date|>",date)
# print(letter)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# days = input(input("enter dayas\n: "))
# fine = 0
# if days<10:
#     fine = (0.40*days)
# elif days<20:
#     fine = (0.40*10)+(days-10)*0.60
# if days>20:
#     fine = (0.40*10)+10*0.60+(days-20)*0.80

# print("the fine amount RS= ",fine)



##########################################################################################################


# price = float(input("enter your price ampount\n: "))
# discount = 0
# if price<=25000:
#     discount = 0
#     gift = 'calculator'
# elif price<=50000:
#     discount = price*5/100
#     gift = 'digital note book'
# elif price <= 100000:
#     discount = price*7.5/100
#     gift = 'wall clock'
# else:
#     discount = price*10/100
#     gift = 'wrist watch'
# net = price-discount
# print("net amount payable RS=",net)
# print("net amount payable RS=",discount)
# print("gift is", gift)

##################################################################################

# days = int(input("No. of days late\n: "))
# fine = 0
# if days<=10:
#     fine = 0.40*days
# elif days<=20:
#     fine = 10*0.40+(days-10)*0.60
# else:
#     fine = 10*0.40+10*0.60+(days-20)*0.80
# print(days, "days late you, thats why your fine is:",fine)

#####################################################################################

# price = float(input("enter your price amount\n: "))
# discount = 0
# if price<=25000:
#     discount = 0
#     gift = ("calculator")
# elif price<=50000:
#     discount = price*5/100
#     gift = ("digital note book")
# elif price<=100000:
#     discount = price*7.5/100
#     gift = ("wall clock")
# else:
#     discount = price*10/100
#     gift = ("wrist watch")
    
# net = price-discount

# print("NET AMOUNT PAYBLE, RS=",net)
# print("your price discount, RS=",discount)
# print("your gift",gift)


#######################################################


# world1 = "FIRST"
# world2 = "first"
# print("world1=",world1,"world2=",world2)
# print(world1>world2) 
# print(world1<world2)
# print(world1==world2)
# print(world1!=world2)
# print(2<4<6>5)
# print(2>4>6<5)

# x="a"
# x=3*x
# print(x)

# x = 3
# num = 17
# print(num % x)

# num = 7
# if num > 3:
#    print("3")
#    if num < 5:
#       print("5")
#       if num ==7:
#          print("7")

# nums = [1, 2, 3, 4, 5]
# nums[3] = nums[2]
# print(nums[3])

# nums = [9, 8, 7, 6, 5]
# nums.append(4) # add last element
# nums.insert(2, 11) #replace the present index[2] to input number[11]
# print(nums)

# i = 3
# while i>=0:
#    print(i)
#    i = i - 1

# i = 5
# while True:
#   print(i)
#   i = i - 1
#   if i <= 2:
#     break



# list = [2, 3, 4, 5, 6, 7]

# for x in list:
#     if(x%2==1 and x>4):
#         print(x)
#         break

# nums = list(range(5))
# print(nums[4])

# nums = list(range(5, 8))
# print(len(nums))

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# while False:
#   print("Looping...")

###################################################

# n = int(input())

# for x in range(3, n,2):
#     if x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#         continue
#     elif x % 3 == 0:
#         print("Solo")
#         continue
#     elif x % 5 == 0:
#         print("Learn")
#         continue
#     else:
#         print(x)

# n = int(input())

# for x in range(1, n,+2):
#     # if x % 3 == 0 and x % 5 == 0:
#     print(x)
       

##################################################

# import qrcode

# img = qrcode.make(
#     '11111111'
# )
# img.save('myQRcode.png')
# img.show()

####################################################

# def hello():
#   print("Hi!")
#   print("Hi!")
#   print("Hi!")
#   print("Hi!")
#   print("Hi!")
#   print("Hi!")
# hello()

################################################

# def print_double(x):
#    print(2 * x)
#    print(4 * x)
#    print(7 * x)

# print_double(3)

################################################

# def even(x):
#   if x%2 == 0:
#     print("Yes")

#   else:
#       print("No")

# even(2)

###################################################

# def shortest_string(x, y):

#   if len(x) <= len(y):
#       print(x)
#       return x
     
#   else:
#       print(y)
#       return y

# shortest_string(8, 6)
###############################################

# def print_numbers():
#   print(1)
#   print(2)
#   return
#   print(4)
#   print(6)
# print_numbers()

############################################

# import math
# import os
# import random
# import re
# import sys

# if __name__ == '__main__':
#     n = int(input())
    
#     if (n%2!=0) or (n>=6 and n<=20):
#         print("weird")
#     else:
#         print("Not Weird")

###############################################

# n = int(input())
# for i in  (0,n):
#     print(i*i)

####################################
# def solveMeFirst(a,b):
#     return a+b
# 	# Hint: Type return a+b below


# num1 = input()
# num2 = input()
# res = solveMeFirst(num1,num2)
# print (res)

######################################

# n=[]
# for i in range(1,11):
#     if i not in n:
#         n.append(i)
#     n.reverse()
# print(n)

######################################
# def print_nums(x):
#   for i in range(x):
#     print(i)
#     return
# print_nums(10)

##############################################


# def conv(c):
#     #your code goes here
#     p = 9/5 * c + 32
#     return p
    

# celsius = int(input("input celsius: "))
# fahrenheit = conv(celsius)
# print(fahrenheit)

####################################

# nums = (55, 44, 33, 22)
# print(max(min(nums[:2]), abs(-42)))

#########################

# lambda
# pass
# map
# __init_
# attribute
# pickling
# namespaces
# class function(A):
# built-in modules are:
#    os
#    math
#    sys
#    random
#    re
#    datetime
#    JSON
# NumPy array
# 1D, 2D and 3D arrays
# pandas dataframe
# finalize
# inheritance
#    Single
#    MULTIPLE
#    multilevel
#    Hierarchical
# OOPS
# iterators
# generators
# pickling and unpickling
# xrange and range
# Scope Resolution
# Scope

##################################

# from audioop import reverse


# l = input("enter a sentence")
# word = l.split()
# op=""
# for i in word:
#     op=" "
#     reverse=i[-1:-len(word)-1:-1]
#     op=op+reverse+" "
# print(op)
    
################################
# l = input("enter a sentence")
# word = l.split()
# list=[]
# o=0
# for i in word:
#     o = len(i)-1
#     list.append(word[o])
#     list.sort()
# print(list)

######################

# import math
# class Plane:
#     def __init__(self,x1,y1):
#         self.x1=x1
#         self.y1=y1
#     def show(self):
#         print("the first coordinate is=(",self.x1,",",self.y1,")")
# class Circle(Plane):
#     def __init__(self,x1,y1,x2,y2):
#         self.x2=x2
#         self.y2=y2
#         Plane.__init__(self,x1,y1)
        
#     def findradius(self):
#         self.r=(math.sqrt(self.x2-self.x1)**2 + (self.y2 - self.y1)**2)/2
    
#     def findarea(self):
#         self.A=(math.pi*self.r*self.r)

#     def show(self):
#         print(f"Length of the radius is {self.r} and are of the circle is {self.A}")

# obj1=Plane(4,6)
# obj1.show()
# obj2=Circle(4,8,6,2)
# obj2.findradius()
# obj2.findarea()
# obj2.show()


##########################################################

# import array as A
# list=[34,-5,-6,-7,2]
# obj=A.array('i',list)

# for i in range(0,obj.itemsize):
#     if i<0:
#        print(i,end=" ")
#     if i>0:
#         print(i,end=" ")

#################################

# class Solution:
#     def __init__(self,List, target):
#         self.List=List
#         self.target=target
        
#     def display(self):
#         l=[]
#         for i in range(len(self.List)):
#             if self.List[i]+self.List[i+1]==self.target:
#                 return first_index
# List = [2,7,11,15]
# # target = 6            
# obj=Solution([2,7,11,15],9)
# print(obj.display())