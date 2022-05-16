
mat=[]
n=0
def fillup():
    global N
    val =1
    rowstart=1
    rowdiff=2
    colddiff=0
    N=int(input("enter the size"))
    for row in range(0,N):
        mat.append([])
        val=rowstart
        colddiff=row
        for col in range(0,N):
            mat[row].append(val)
            val=val+colddiff
            colddiff=colddiff+1
        rowstart=rowstart+rowdiff
        rowdiff=rowdiff+1

def display():
    print("output=")
    for i in range(0,N):
        for j in range(0,N):
            print(mat[i][j],end=" ")
        print()

#main
fillup()
display()
