# Enater a word: GREAT
# Output
#G
#GR
#GRE
#GREA
#GREAT

line=input("enter a word ->")
word=len(line)

for i in range(1,word+1):
    print(line[0:i])

