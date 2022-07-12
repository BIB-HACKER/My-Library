#pig latin

word=input("enter a word :")
# word=word.upper()
length=len(word)
add="aeiou"
ADD="AEIOU"

for i in range(length):
  ch=word[i]
  if ch in add:
    op=word[i:length]+word[0:i]+"ay"
    print("piglatin word is=",op)
    break
  if ch in ADD:
    op=word[i:length]+word[0:i]+"AY"
    print("piglatin word is=",op)
    break
else:
  print("piglatin word is not possible")
    