#Display all 3 digits palindromic numbers using UDF

def ispalindrome(num):
    rev=0
    copy=num
    while copy>0:
        rev=rev*10+copy%10
        copy=copy//10
    if rev==num:
        return True
    else:
        return False
#main
for val in range(100,10000):
    if ispalindrome(val):
        print(val,end=" ")
    
