#input a year and check weather the year is a leap year or not
#A century year is a leap year if it is divisible by 400
#A non-century year is a leap year if it is divisible by 4


year = int(input("enter the year\n: "))
if year%100==0:   #cheak for century year
    if year%400==0:
        print(year,"is a lep year")
    else:
        print(year,"is a not lep year")    
else:   #cheak for non-century year
    if year%4==0:
        print(year,"is a lep year")
    else:
        print(year,"is not a lep year")

print("end the program") 

#########################################################################################

year = int(input("enter the year\n: "))
if year>=100:
    print(year, "this is a century year")
else:
    print(year, "this is a not century year")
