#Nested loop
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7

def displaypattern(row):
    for outer in range(1,row+1):
        for inner in range(1,outer+1):
            print(inner,end=" ")
        print()
row=int(input("how many rows to print"))
displaypattern(row)