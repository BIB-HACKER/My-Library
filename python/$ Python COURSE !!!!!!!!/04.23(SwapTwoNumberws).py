# swap two numbers using-defined method(swapping occurs within function only)
def swap(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    print("within the method")
    print("num1=",num1,"num2=",num2)

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
swap(num1,num2)#method call
print("after function call")
print("num1=",num1,"num2=",num2)
