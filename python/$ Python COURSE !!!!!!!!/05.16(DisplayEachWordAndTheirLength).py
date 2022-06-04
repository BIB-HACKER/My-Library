#input a line and display the words along with total numbers of characters present in each of the word
#this method task input a line,splits wordwise and stores in a list.at last returns the list
def getinput():
    line=input("input a line->")
    words=line.split()
    return words

def display(words):
    print("word","no. of chracters")
    for word in words:
        print(word,"   ",len(word))
#main
words=getinput()
display(words)