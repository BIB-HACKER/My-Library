#Nested Loop

# 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9

def displaypattern(row):
    for outer in range(1,row+1):
        for inner in range(1,row+1):
            print(outer,end=" ")
        print()
row=int(input("how many rows to print"))
displaypattern(row)