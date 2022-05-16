num = int(input("enter more then 9 num "))
evensum = 0
oddsum = 0

if num<10:
    print("this is invalid number")
else:
    # while num>0:
    for di in range(0,num):
        digit = num%10
        if digit%2==0:
            evensum+=digit
        else:
            oddsum+=digit 

        num//10

    if evensum==oddsum:
        print("this is a special number")
    else:
        print("this is not a spacial umber")