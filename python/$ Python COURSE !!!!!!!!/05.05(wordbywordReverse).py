# input a sentence. then reverse each word and a new sentence

words=input("enter a sentence")
word=words.split()
rev=""
for i in  word:
    reverse=i[-1:-len(i)-1:-1]
    rev=rev+reverse+" "

print(rev)
