# input a sentence and display only the palindromic number
line=input("enter a line ->")
words=line.split() #here words is a list of strings
print("Palindromic words are :-")
for word in words:
    rev="" #create an empty string
    # Generates reverse of the string
    for ch in word:
        rev=ch+rev
    if rev.upper()==word.upper():
        print(word)

# rev=""
# for ch in line:
#     rev=ch+rev
# print(rev)
