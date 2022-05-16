#create a list 
# count less then 30odd values and more then 50even values 

l = eval(input("enter 10 integers in a list"))
countodd=0
counteven=0
print("all the odd numbers which are less then 30")
for odd in l:
    if odd%2==1 and odd<30:
        print(odd)
        countodd=countodd+1
print("all the even numbers which are more then 50:-")
for even in l:
    if even%2==0 and even>50:
        print(even)
        counteven=counteven+1
print("total odd numbers are less then 30", countodd)
print("total odd numbers are more then 50", counteven)