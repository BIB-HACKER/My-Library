#INPUT A NAME AND DISPLAY INITIALS WITH DOTS
name = input("enter your full name= ")
words=name.split()
fen=""
for word in words:
    word=word.capitalize()
    fen=fen+word[0]+"."
print("output word is= ",fen)