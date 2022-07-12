#ARRAYS IN PYTHON
def mergetwosortedarrays(arr1,arr2):

    i=0
    j=0
    len1=len(arr1)
    len2=len(arr2)

    arr=[]
    while (i<len1) and (j<len2):
        if (arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    # print(arr)
    while i<len1:
        arr.append(arr1[i])
        i+=1
    while j<len2:
        arr.append(arr2[j])
    return arr

    ##################################

    # for i in arr1:
    #     arr.append(i)
    # for j in arr2:
    #     arr.append(j)
    # arr.sort()
    # return arr
    
    ##################################

    # for i in arr1:
    #     if i not in arr:
    #         arr.append(i)
    # for j in arr2:
    #     if j not in arr:
    #         arr.append(j)
    # arr.sort()
    # return arr
    
#main
arr1=[1,4,6,8,10]
arr2=[2,3,5,7,9]
# arr1=[1,4,6,7,8,10]
# arr2=[2,3,4,5,7,9]
arr=mergetwosortedarrays(arr1,arr2)
print(arr)