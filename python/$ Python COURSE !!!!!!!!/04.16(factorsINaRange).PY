#Display Factors of all the numbers between a range using UDF

def displyfactors(lower,upper):
    for val in range(lower,upper+1):
        print("\nfactorials of",val,"is :")
        for factors in range(1,val+1):
            if val%factors==0:
                print(factors,end=" ")
#main
lower = int(input("choose lower number"))
upper = int(input("choose upper number"))

if lower>upper:
    print("invalid input")

else:
    displyfactors(lower,upper)