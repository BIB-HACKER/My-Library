#display first n finonacci numbers
# 0 1 1 2 3 5 8 13 21 34
def fib(n):
    if n<=1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
# fib(3)
# return fib(2)+ fib(1)
# return 1+ 0
# return 1

# fib(7)
# return fib(6)+ fib(5)
# return fib(5)+ fib(4)+ fib(4)+ fib(3)
# return fib(4)+ fib(3)+ fib(3)+ fib(2)+ fib(3)+ fib(2)+ fib(2)+ fib(1)
# return fib(3)+ fib(2)+ fib(2)+ fib(1)+ fib(2)+ fib(1)+ 1+ fib(2)+ fib(1)+ 1+ 1+ 0
# return fib(2)+ fib(1)+ 1+ 1+ 0+ 1+ 1+ 1+ 0+ 2
# return 1+ 0+ 7
# return 8

n=int(input("enter total number of terms->"))
for i in range(1,n+1):
    print(fib(i),end=" ")