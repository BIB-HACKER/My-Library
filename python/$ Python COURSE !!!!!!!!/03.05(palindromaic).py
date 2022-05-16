#input a number and check weather the number is palindromic no or not (palindromic no.-->121,11,12321,22,33 -- like a morror )

num=int(input("enter a positive number"))
rev=0
copy=num
while num>0:
    rev = rev*10 + num%10
    num//=10
if copy==rev:
    print("this is a palindromic no")
else:
    print("this is a not palindromic no")

###################################################

#input a number and check weather the number is palindromic no or not (palindromic no.-->121,11,12321,22,33 -- like a morror )

print("palindromic numbers between 10 to 200 are =")
num = 10
while num<=200:
    rev=0
    copy=num
    while copy>0:
        rev = rev*10 + copy%10
        copy//=10
    if num==rev:
        print(num, end=" ")
    num+=1