num=int(input("enter a number"))
copy=num
rev=0
while num>0:
    rev=rev*10 + num%10
    num//=10

if copy==rev:
    print("this is a palindrome number")
else:
    print("this not a palindrome number")
