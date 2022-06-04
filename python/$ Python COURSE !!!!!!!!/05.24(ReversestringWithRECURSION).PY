#Display a string in reverse by recursive method
def reversestring(word):
    if len(word)==0:
        return ""
    else:
        print(word[len(word)-1],end="")
        reversestring(word[:len(word)-1])

#word="python"
#reversestrig("python")
# print(n)
# reversestring("pytho")
# print(no)
# reversestring("pyth")
# print(noh)
# reversestring("pyt")
# print(noht)
# reversestring("py")
# print(nohty)
# reversestring("p")
# print(nohtyp)#################
# reversestring("")
#return ""

word=input("enter a word->")
reversestring(word)