#write a program to accept a sentence and perform the following task:
#(a) arrange the words contained in the sentence according to the size fo the words in asending order.
#if tow words are of teh same length then the first occurring comes first.
#(b) count numbeer of words starting with vowel.
#Example:
#Input: A STITCH IN TIME SAVES NINE
#Output: 
#AFTER ARRANGEING: A IN TIME NINE SAVES STITCH
#NO OF WORDS: 02

line= input("enter a sentence->")
wordslist=line.split()
op=""
#BUBBLE SORT
for i in range(1,len(wordslist)):
    for j in range(0,len(wordslist)-i):
        if (len(wordslist[j])>len(wordslist[j+1])):  #swapping code

            # temp=wordslist[j]
            # wordslist[j]=wordslist[j+1]
            # wordslist[j+1]=temp
            wordslist[j],wordslist[j+1]=wordslist[j+1],wordslist[j]

count=0
vowelset=('a','e','i','o','u','A','E','I','O','U')
for word in wordslist:
    if word.startswith(vowelset):
        count+=1
    op+=word+" "
print("output")
print(op)
print("No of words starting with vowel=",count)

