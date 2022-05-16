#INPUT A NUMBER AND CHECK THE NUMBER IS A PALINDROMIC NUMBER OR NOT USING UDF

# def isPalindrome(num):
#     rev = 0
#     copy=num
#     while copy>0:
#         rev=rev*10+copy%10
#         copy=copy//10
#     if rev==num:
#         print("this is a palindrome numebr")
#     else:
#         print("this is not a palindrome number")
    

# #main
# n=int(input("enter a positive numebr"))
# isPalindrome(n)

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

def isPalindrome(num):
    rev = 0
    copy=num
    while copy>0:
        rev=rev*10+copy%10
        copy=copy//10
    if rev==num:
        return True
    else:
        return False
    
#main
n=int(input("enter a positive numebr"))
check=isPalindrome(n)
if check==True:
    print("this is a palindrome numebr")
else:
    print("this is not a plaindrom number")
    