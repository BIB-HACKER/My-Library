#Count frequency--liner search 
def getcount(line,ch):
    count=0
    for char in line:
        if char.lower()==ch.lower():
            count+=1
    return count

line=input("enter a sentence ->")
ch=input("enter a character to search->")
count=getcount(line,ch)
if count==0:
    print("the character is found",count,"times")
else:
    print("the character is found",count,"tims")
    