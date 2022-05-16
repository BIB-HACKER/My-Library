def abcdefg(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

#main
num=int(input("enter number"))
factorial=abcdefg(num)
print("the factoral of",num,"is",factorial)
# num=int(input("enter number"))
# print("the factoral of",num,"is",abcdefg(num))


