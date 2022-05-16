# input length and breath of a rentengle. input choice form user. if user's
#choice is 1 then find and display area of the rectengle
# if user's chice is 2 then find and display perimeter of the rectengle




# length = int(float(input("enter length of a rectengle in cm ")))
# breath = int(float(input("enter breath of a rectengle in cm ")))
# print ("enter 1 for displaying area or enter 2 for displaying perimeter")
# choice = int(input("enter your choice(1/2)"))
# if choice==1:
#     area=length * breath
#     print("area of the rentangle =", area, "sq cm")
# elif choice==2:
#     peri=2*(length * breath)
#     print("perimetr =",peri, "sq cm")
# else:
#     print("invalid choice")



######################################################################################
#

                                      #SQURE

length = int(float(input("enter length of a squre in cm ")))
print ("enter 1 for displaying area or enter 2 for displaying perimeter")
choice = int(input("enter your choice(1/2)"))
if choice==1:
    area=length**2
    print("area of the rentangle =", area, "sq cm")
elif choice==2:
    peri=4*length
    print("perimetr =",peri, "sq cm")
else:
    print("invalid choice")

###################################################################

                             #CIRCULE

radius = int(float(input("enter circle radius\n: ")))
print ("enter 1 for displaying area, or enter 2 for displaying diameter, and 3 for displaying circumference")
choice = int(input("enter your choice(1/2/3)"))
if choice==1:
    area=3.14*radius**2
    print("circle of are =", area)
elif choice==2:
    diameter=2*radius
    print("cicle of diametr =",diameter)
elif choice==3:
    circumference=2*3.14*radius
    print("circle of circumference =",circumference)
else:
    print("invalid choice")
