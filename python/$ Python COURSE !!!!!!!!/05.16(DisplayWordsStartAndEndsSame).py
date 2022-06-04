#input a line and display the words which start and end with same letter
#this method returns true if the parameter word starts and ends with same letters

def isstartandendsame(word):

    # word=word.upper()
    # if word[0]==word[len(word)-1]:
    #     return True
    # else:
    #     return False

    return word.upper().endswith(word[0].upper())

#takes input a line and display the words which start and end with same letter
def getinput():
    line=input("enter a sentence->")
    words=line.split()
    print("output:")
    count=0
    for word in words:
        if isstartandendsame(word):
            print(word)
            count+=1
    print("no of same end and start word is=",count)
            

getinput()

