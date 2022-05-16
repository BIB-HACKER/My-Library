# a number is a sepecial number it sum of digit is equal to the product of digit.

lower = int(input("enter lower limit"))
upper = int(input("enter upper limit"))
if lower>upper:
    print("invalid input")
else:
    print("special number are=")

    while lower<=upper:
        sum=0
        product=1
        copy=lower
        while copy>0:
            sum+=copy%10
            product*=copy%10
            copy//=10
        if sum==product:
            print(lower,end=" ")
        lower+=1