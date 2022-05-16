print ("enter choice 1: or enter choice 2:")
choice = int(input("enter your choice(1/2)"))

if choice==1:
    term = 1
    tom = -4
    for i in range (1,11):
        print(term)
        print(tom)
        term= term+6
        tom= tom-6
       
elif choice==2:
    for i in range (1,101):
     if i%10==7 or i%7==0:
       print(i)
    #  else:
    #    print("this number is not buzz number=", i)



        
    



