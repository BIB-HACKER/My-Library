# 2 2 2 2  2  2  2  2  2   2  
# 1 2 3 4  5  6  7  8  9  10
# 2 4 6 8 10 12 14 16 18  20

first=[]
second=[]
third=[]
val=int(input("Enter your choice number"))
for i in range(1,11):
    second.append(i)
    num=val*i
    first.append(val)
    third.append(num)
bibhakar=(first,second,third)
rows=len(bibhakar)
cols=len(bibhakar[0])
print("The table is=")
for i in range(0,rows):
    for j in range(0,cols):
        print(bibhakar[i][j],end=" ")
    print()