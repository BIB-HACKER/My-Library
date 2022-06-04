#enter a line and display the palindromic words only

#returns true if the parameter word is a palindrome otherwise returns false
def ispalindrome(word):
    rev=""
    for i in range(len(word)):
        rev=word[i]+rev  #reverse string
    if rev.upper()==word.upper():
        return True
    else:
        return False

#takes input a line and display the palindrome words
def getinput():
    line=input("enter a line/sentence->")
    words=line.split()
    print("Output:")
    print("Palindromic words are:")
    count=0
    for word in words:
        if ispalindrome(word):
            print(word)
            count+=1
    
    if count==0:
        print("no palindromic word is present in the line")
    
#main 
getinput()