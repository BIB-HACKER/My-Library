'''INPUT =

   TAKE THE NUMBER OF INUPT AS INTEGER 'N'
   TAKE THE ALPHANUMERIC STRING 'S' AS INPUT.
   
   OUTPUT =

   PRINT ONLY THE NUMERIC POSITION OF THE CHRACTERS PRESENT IN THE ALPHANUMERIC STRING 'S'.
'''
print("INPUT: ")
N=int(input("enter number ->"))
S=[]

for i in range(0,N):
    S.append(input("enter string ->"))
print("OUTPUT: ")
for j in S:
    for i in range(0,len(j)):
        if j[i].isalpha():
            print(i,end="")
    print()


    