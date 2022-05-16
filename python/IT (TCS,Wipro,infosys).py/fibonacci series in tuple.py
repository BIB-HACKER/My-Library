first = 0 
second = 1
print("all the fibonacci number between 0 and num are")
N = []
third = 0
num = int(input("ENTER YOUR LIMIT NUMBERS :"))
for i in range(1,num):
    third = first+second
    N.append(third)
    first=second
    second=third
print(N)