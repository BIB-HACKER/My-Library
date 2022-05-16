# Nested lsit --- Row wise list sort
mat=[]
row=0
col=0
def getinput():
    global row
    global col
    #create sublist in list
    row=int(input("how many rows"))  ###########
    col=int(input("how many colums")) ###############
                                       #############                
    for i in range(0,row):               ###########                 
        mat.append([])                    ##############
        for j in range(0,col):             ########                  
            mat[i].append(int(input("enter a number")))##########

def display():
    print("original lsit is")
    #display in matrix format
    for i in range(0,row):
        print(mat[i])

def dosort():

    #Rowwise sort
    for i in range(0,row):
        mat[i].sort()
    #Display the sorted list
    print("the sorted list is=")
    for i in range(0,row):
        print(mat[i])


getinput()
display()
dosort()