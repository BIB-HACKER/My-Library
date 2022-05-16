#swap two numbers using-defined method
def swap():
    global num1
    global num2
    #swapping code
    temp=num1
    num1=num2
    num2=temp
    print("within the method")
    print("num1=",num1,"num2=",num2)

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
swap()#method call
print("after funtion call")
print("num1=",num1,"num2=",num2)